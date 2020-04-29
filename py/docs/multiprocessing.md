# multiprocessing

```
import multiprocessing as mp
lane_img_dfs = np.array_split(self.lane_img_df, jobs)
pool = mp.Pool(jobs)
pool_input = zip([self]*jobs, lane_img_dfs, [eyeq_version]*jobs, [method]*jobs, [even_sampling]*jobs)
self.lane_img_df = pool.map(scores_evaluation_wraper, pool_input)  
self.lane_img_df = pd.concat(self.lane_img_df, ignore_index=True).sort_values("time")

def scores_evaluation_wraper(data):
    """
    """
    self, lane_img_df, eyeq_version, method, even_sampling = data
    self.lane_img_df = lane_img_df.reset_index()
    scores = []
    left_time_diffs = []
    right_time_diffs = []

```