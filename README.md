# IllustGen
Service Designed by Team devBricks since Dec. 2021

## overview
[1] 웅진북센 주최 2021 한국어 말뭉치를 이용한 인공지능 서비스 공모전 출품작

[2] Flask & DALL-e VAE를 사용한 이미지 생성 구현 서비스 기획, 개발

## Flask Application
예시 화면
![image](https://user-images.githubusercontent.com/40736396/147096513-2d63a72d-f507-4122-9b33-18ca5b2fdbac.png)

![image](https://user-images.githubusercontent.com/40736396/147096602-f1835c12-05c2-4097-aaa9-a564ec1f3197.png)

![image](https://user-images.githubusercontent.com/40736396/147096643-47e0cbd6-7431-4f25-8e44-ee46daaadbb8.png)

## DALL-e Usage

예시 화면

[1] Train VAE
`
$ python train_vae.py --image_folder /path/to/your/images
`

[2] Train DALL-e
`
$ python train_dalle.py --vae_path ./vae.pt --image_text_folder /path/to/data
`

`
$ python train_dalle.py --dalle_path ./dalle.pt --image_text_folder /path/to/data
`

[3] you can then used the saved model for generation!
`
$ python generate.py --dalle_path ./dalle.pt --text '<내용입력>'
`
## Dependency
[1] [DALL-e](https://openai.com/blog/dall-e/) & DALL-E in pytorch 
