# 동작 
full video: https://www.youtube.com/watch?v=gZ1vCTqO5TA
| ![1](https://github.com/user-attachments/assets/56f7b647-02dd-4441-9bf3-6bf952d4d1bd) | ![2](https://github.com/user-attachments/assets/33e520cb-847f-42c1-adf2-0afc4acdc9d0) |
|----------|----------|
| ![스크린샷 2024-12-26 14-58-40](https://github.com/user-attachments/assets/e6c92e45-7e93-4c56-b969-72c59f1e2f6b) | ![스크린샷 2024-12-26 14-57-17](https://github.com/user-attachments/assets/a893b7f3-31c8-4d91-8aca-c056dd6dc0b6) |

</br>  

# 실행
```
sh run.sh
gazebo --verbose ripple.world
```

</br>

#### 수정 반영
```
rm -rf ~/.gazebo/paging/ripple; gazebo --verbose
```
수정 후 다시 실행하려면 캐시 지워야 함

</br>  

#### sdf 파일 만드는 코드
```
python3 ripple_sdf_case.py 
```
모든 경우에 대한 sdf 파일을 만들어서 저장해 줌   
그러나 visual의 uri의 경우 아래 조건을 만족해야 함  
즉, track.png가 uri인 것은 제대로 동작하지 않음

| rrr.png | rtr.png | trr.png | ttr.png |
|----------|----------|----------|----------|
| ![rrr](https://github.com/user-attachments/assets/4d2fa20c-72d3-4581-9b94-39abf2925ebb) | ![rtr](https://github.com/user-attachments/assets/3ef13969-4625-4db5-9694-487a6fad62cd) | ![trr](https://github.com/user-attachments/assets/8ccf1d2e-c878-48a5-9828-2d62534302fa) | ![ttr](https://github.com/user-attachments/assets/5b012f2d-d590-4e63-a7d0-4f358138c766) |

</br>  

#### 이미지 리사이즈 코드
리플 이미지를 다른 이미지로 대체해도 되지만 사이즈가 2^n+1이어야 함
<details>
<summary>code 보기</summary>

```
import cv2
import os

# 이미지 불러오기
image_path = 'test.png'
image = cv2.imread(image_path)

# 이미지의 크기 확인
height, width, _ = image.shape
print(f"Image size: {height}x{width}")

# 자를 크기
crop_size = 513

# 이미지 크기 조정 (513x513)
resized_image = cv2.resize(image, (crop_size, crop_size))

# 이미지를 자르기
for y in range(0, height, crop_size):
    for x in range(0, width, crop_size):
        # 이미지의 일부 자르기 (좌상단 좌표(x, y), 크기(crop_size, crop_size))
        cropped_image = resized_image[y:y + crop_size, x:x + crop_size]
        cv2.imwrite(f"cropped_{y}_{x}.png", cropped_image)
```
</details>
