
#!/bin/bash

# 복사 대상 폴더와 파일
SOURCE_DIR="./track_with_ripple"

# 대상 경로 설정
GAZEBO_DIR="/home/$(whoami)/.gazebo"

# 대상 디렉토리가 존재하지 않으면 생성
if [ ! -d "$GAZEBO_DIR" ]; then
    echo "Creating target directory: $GAZEBO_DIR"
    mkdir -p "$GAZEBO_DIR"
fi
MODELS_DIR="$GAZEBO_DIR/models"
if [ ! -d "$MODELS_DIR" ]; then
    echo "Creating target directory: $MODELS_DIR"
    mkdir -p "$MODELS_DIR"
fi

# 폴더 및 내용물 복사
if [ -d "$SOURCE_DIR" ]; then
    echo "Copying $SOURCE_DIR to $MODELS_DIR"
    cp -r "$SOURCE_DIR" "$MODELS_DIR"
    echo "Copy completed successfully."
else
    echo "Source directory $SOURCE_DIR does not exist. Aborting."
    exit 1
fi

