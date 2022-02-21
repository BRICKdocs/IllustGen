from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
import os, sys, argparse, clip
from .minDALLE.dalle.models import Dalle
from .minDALLE.dalle.utils.utils import set_seed, clip_score
import numpy as np
from PIL import Image

device = 'cpu' # gpu 달려있으면  cuda 셋팅 후 전환
set_seed(0)

prompt = "description" # 텍스트 데이터를 여기서 수신 받아야함  promptRx
model = Dalle.from_pretrained('minDALL-E/1.3B')  # This will automatically download the pretrained model.
model.to(device=device)

# Sampling
images = model.sampling(prompt=prompt,
                        top_k=128, # It is recommended that top_k is set lower than 256.
                        top_p=None,
                        softmax_temperature=1,
                        num_candidates=4, # device 성능에 의존. 수치를 낮출수록 생성속도가 빨ㄹ라짐
                        device=device).cpu().numpy()
images = np.transpose(images, (0, 2, 3, 1))

# CLIP Re-ranking
model_clip, preprocess_clip = clip.load("ViT-B/32", device=device)
model_clip.to(device=device)
rank = clip_score(prompt=prompt,
                images=images,
                model_clip=model_clip,
                preprocess_clip=preprocess_clip,
                device=device)

# Plot images ==> 결과 데이터를 여기서 보내줘야 함
plt.switch_backend('Agg') # Agg as Matplotlib backend
images = images[rank]
plt.imshow(images[0]) # imgTx
fname = str(hash(id(images[0])))

"""
if not os.path.exists('./static/imagegen'):
    os.makedirs('./static/imagegen')
for i in range(min(16, args.num_candidates)):
    im = Image.fromarray((images[i]*255).astype(np.uint8))
    im.save(f'./static/imagegen/{args.prompt}_{i}.png')
"""
plt.show()
plt.savefig("./static/imagegen/"+fname+".png")


