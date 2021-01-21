# thread_pool.h

```
#ifndef CYBER_BASE_THREAD_POOL_H_
#define CYBER_BASE_THREAD_POOL_H_

#include <atomic>
#include <functional>
#include <future>
#include <memory>
#include <queue>
#include <stdexcept>
#include <thread>
#include <utility>
#include <vector>

#include "cyber/base/bounded_queue.h"

namespace apollo {
namespace cyber {
namespace base {

class ThreadPool {
 public:
  explicit ThreadPool(std::size_t thread_num, std::size_t max_task_num = 1000);

  template <typename F, typename... Args>
  //https://blog.csdn.net/weixin_33795833/article/details/88703536
  //&&右值引用，这个功能自C++11起才可用。移动语义是C++11新增的重要功能，其重点是对右值的操作。右值可以看作程序运行中的临时结果，右值引用可以避免复制提高效率。
  auto Enqueue(F&& f, Args&&... args)
      -> std::future<typename std::result_of<F(Args...)>::type>;

  ~ThreadPool();

 private:
  std::vector<std::thread> workers_;
  BoundedQueue<std::function<void()>> task_queue_;
  //https://blog.csdn.net/xidaoliang/article/details/79713283
  //C++中atomic 数据类型操作
  //它表示在多个线程访问同一个全局资源的时候，能够确保所有其他的线程都不在同一时间内访问相同的资源。也就是他确保了在同一时刻只有唯一的线程对这个资源进行访问。这有点类似互斥对象对共享资///源的访问的保护，但是原子操作更加接近底层，因而效率更高。
  std::atomic_bool stop_;
};

inline ThreadPool::ThreadPool(std::size_t threads, std::size_t max_task_num)
    : stop_(false) {
  if (!task_queue_.Init(max_task_num, new BlockWaitStrategy())) {
    throw std::runtime_error("Task queue init failed.");
  }
  workers_.reserve(threads);
  for (size_t i = 0; i < threads; ++i) {
    //https://zhidao.baidu.com/question/460842124417071845.html
    //lamba表达式，参考上面的链接，现在的理解感觉是给std::thread一个匿名的函数作为其构造函数
    workers_.emplace_back([this] {
      while (!stop_) {
        std::function<void()> task;
        if (task_queue_.WaitDequeue(&task)) {
          task();
        }
      }
    });
  }
}

// before using the return value, you should check value.valid()
template <typename F, typename... Args>
auto ThreadPool::Enqueue(F&& f, Args&&... args)
    -> std::future<typename std::result_of<F(Args...)>::type> {
  using return_type = typename std::result_of<F(Args...)>::type;

  auto task = std::make_shared<std::packaged_task<return_type()>>(
      std::bind(std::forward<F>(f), std::forward<Args>(args)...));

  std::future<return_type> res = task->get_future();

  // don't allow enqueueing after stopping the pool
  if (stop_) {
    return std::future<return_type>();
  }
  task_queue_.Enqueue([task]() { (*task)(); });
  return res;
};

// the destructor joins all threads
inline ThreadPool::~ThreadPool() {
  if (stop_.exchange(true)) {
    return;
  }
  task_queue_.BreakAllWait();
  for (std::thread& worker : workers_) {
    worker.join();
  }
}

}  // namespace base
}  // namespace cyber
}  // namespace apollo

#endif  // CYBER_BASE_THREAD_POOL_H_

```