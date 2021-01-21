# README
- http://c.biancheng.net/cplus/11/
- https://github.com/DragonFive/cpp11
- https://changkun.de/modern-cpp/
- https://github.com/AnthonyCalandra/modern-cpp-features/blob/master/CPP11.md
- https://github.com/huangmingchuan/Cpp_Primer_Answers
- https://github.com/jaredtao/DesignPattern

- [std::future](https://blog.csdn.net/lijinqi1987/article/details/78507623)
```
std::result_of 编译时类型推导
struct S {
    double operator()(char, int&); // 这个函数的返回类型是 double
};

int main()
{

    std::result_of<S(char, int&)>::type foo = 3.14; // 使用这样的写法会推导出模板参数中函数的返回值类型
    typedef std::result_of<S(char, int&)>::type MyType; // 是 double 类型吗?
    std::cout << "foo's type is double: " << std::is_same<double, MyType>::value << std::endl;
    return 0;
}

std::calloc
一般使用后要使用 free(起始地址的指针) 对内存进行释放。
跟malloc的区别：
calloc在动态分配完内存后，自动初始化该内存空间为零，而malloc不初始化，里边数据是随机的垃圾数据。


pool_ = reinterpret_cast<T*>(std::calloc(pool_size_, sizeof(T)));


std::condition_variable
当 std::condition_variable 对象的某个 wait 函数被调用的时候，它使用 std::unique_lock(通过 std::mutex) 来锁住当前线程。当前线程会一直被阻塞，直到另外一个线程在相同的 std::condition_variable 对象上调用了 notification 函数来唤醒当前线程。

std::condition_variable 对象通常使用 std::unique_lock<std::mutex> 来等待，如果需要使用另外的 lockable 类型，可以使用 std::condition_variable_any 类，本文后面会讲到 std::condition_variable_any 的用法。

```