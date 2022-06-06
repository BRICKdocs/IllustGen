import base64
from io import BytesIO

### For MacOS##
import matplotlib
matplotlib.use('Agg') #switch_backend
import matplotlib.pyplot as plt
###############

import clip
from ..minDALLE.dalle.models import Dalle
from ..minDALLE.dalle.utils.utils import set_seed, clip_score
import numpy as np

from matplotlib.figure import Figure
from re import DEBUG
from flask import blueprints, url_for, render_template, flash, request, session, g
from werkzeug.utils import redirect

bp = blueprints.Blueprint('gen', __name__, url_prefix='/gen')

@bp.route('/loading')
def loading():
    return render_template('gen/loading.html')

@bp.route('/minting')
def minting():
    return render_template('gen/minting.html')

@bp.route('/nft_done/<description>')
def done(description):        
    return render_template('gen/nft_done.html', fname=description.replace(' ','_')+'.png')
    
@bp.route('/result/<description>', methods=('GET', 'POST'))
def result(description):
    
    if request.form.get('mint-pic'):
        return redirect(url_for('gen.done', description=description))

    device = 'cpu' # gpu 달려있으면  cuda 셋팅 후 전환
    set_seed(0)

    prompt = description # 텍스트 데이터를 여기서 수신 받아야함  promptRx

    model = Dalle.from_pretrained('minDALL-E/1.3B')  # This will automatically download the pretrained model.
    model.to(device=device)

    # Sampling
    images = model.sampling(prompt=prompt,
                            top_k=256, # It is recommended that top_k is set lower than 256.
                            top_p=4,
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
    images = images[rank]
    plt.imshow(images[0]) # imgTx
    plt.axis('off')
    # plt.show()
    buf = BytesIO()
    # fname = str(hash(id(Figure[0])))
    plt.savefig(buf, format="png")
    imgname = description.replace(' ','_')+'.png'
    plt.savefig('app/static/gen_result/'+imgname)
    #Embed the result in the html output
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    data = f'data:imagegen/png;base64,{data}'
        # "./static/imagegen/"+fname+".png"
    # plt.imshow(images[0]) # imgTx
    # Image.fromarray((images[i]*255).astype(np.uint8))
    return render_template('gen/result.html', fname=imgname, title=description) # --> api call --> react receive 
    
    #웹페이지 테스트시 위까지 코멘트 아래줄 언코멘트
    #return render_template('gen/result.html', title=description)
'''
@bp.route('/result', methods=['POST'])
def go_mint():
    if request.form.get('mint-pic'):
        return redirect(url_for('gen.done'))
'''