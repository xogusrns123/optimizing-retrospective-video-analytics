from QueryProcessor import QueryProcessor
from configs import TrajectoryConfig, BackgroundConfig
from VideoData import VideoData
# import sys


if __name__ == "__main__":
    # 환경변수설정
    # sys.path.append('/home/kth/URP/optimizing-retrospective-video-analytics/models/research')
    # sys.path.append('/home/kth/URP/optimizing-retrospective-video-analytics/models/research/slim')

    traj_conf = TrajectoryConfig(diff_thresh=1, chunk_size=60)
    video_data = VideoData(db_vid="auburn_first_angle", hour=3)
    bg_conf = BackgroundConfig(peak_thresh= 1)
    Query = QueryProcessor(query_type= "bbox", video_data= video_data, model= "coco", query_class= 2, # "car"
                            query_conf= None, mfs_approach= 0.5, bg_conf= bg_conf, traj_conf= traj_conf, ioda= None, query_segment_size= 30)
    Query.execute(1,1)

    print("end query")