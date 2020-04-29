# UnitTest

```
import unittest
class TestDfs(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.env_variable = 'PYTHONPATH=/opt/ros/melodic/lib/python2.7/dist-packages'

    def test_bad_lane_filter(self):
        #bash_cmd = 'python3 app/lane_compare.py {} && exit'.format(replay_dir)
        #bash_command="docker exec -it -e {} dfs bash -c '{}'".format(self.env_variable, bash_cmd)
        py_cmd = 'python3 app/filter.py --data_path=/home/data/rawdata/2019-10-29-19-42 --filter_type=bad_lane'
        bash_command = "docker exec -it -e {} dfs bash -c '{}'".format(self.env_variable, py_cmd)
        logging.info('filtet command is ....{}'.format(bash_command))
        os.system(bash_command)

if __name__ == '__main__':
    unittest.main()        
```