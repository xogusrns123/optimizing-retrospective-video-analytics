# 2023 Winter/Spring KAIST URP PROGRAM

# A Pilot Study for Co-optimizing Large-Scale Retrospective Video Analytics

Simple overview of use/purpose.

## Description

An in-depth paragraph about your project and overview of use.

## Getting Started

### Dependencies

    opencv, pandas, scipy, tqdm, munkres, numpy
    python=3.7

    cudatoolkit=11.8.0
    nvidia-cudnn-cu11==8.6.0.163
    tensorflow=2.12.1
    tensorflow object_detection API
    matplotlib
    mongoengine
    protobuf==3.6.1
    hwang requires protobuf==3.6.1

    1. install protobuf
        hwang install때문에 virtual env가 아닌 base에서 protobuf install하기 (hwang이 virtual env의 protobuf를 찾지를 못함)

        ```
        wget https://github.com/protocolbuffers/protobuf/releases/download/v3.6.1/protobuf-all-3.6.1.tar.gz
        tar -xvf protobuf-all-3.6.1.tar.gz
        cd protobuf-3.6.1
        ./autogen.sh
        ./configure
        make
        make check
        sudo make install
        sudo ldconfig
        ```
        check correctly installed
        ```
        protoc --version
        ```

    2. install tensorflow
        tensorflow==2.3.0, cuDNN==7.6, cuda==10.1

    3. install hwang

    export LD_LIBRARY_PATH=/home/kth/URP/optimizing-retrospective-video-analytics/hwang/build$LD_LIBRARY_PATH

    4. object detection


현재 protobuf 3.6.1이 아님. tensorflow때문에 버전 맞출려고 protobuf는 더 최신 버전이다.
따라서, protbuf를 3.6.1로 해야하고 tensorflow는 이에 맞게 더 낮은 버전을 사용해야한다.
    


* Describe any prerequisites, libraries, OS version, etc., needed before installing program.
* ex. Windows 10

### Installing
1. config file의 main_dir 세팅하기
* How/where to download your program
* Any modifications needed to be made to files/folders

### Executing program

* How to run the program
* Step-by-step bullets
```
code blocks for commands
```

## Help

Any advise for common problems or issues.
```
command to run if program contains helper info
```

## Authors
Taehyun Kim, KAIST 

* xogusrns123@kaist.ac.kr

## Version History

* 0.2
    * Various bug fixes and optimizations
    * See [commit change]() or See [release history]()
* 0.1
    * Initial Release

## License

This project is licensed under the [taehyunkim] License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [dbader](https://github.com/dbader/readme-template)
* [zenorocha](https://gist.github.com/zenorocha/4526327)
* [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)