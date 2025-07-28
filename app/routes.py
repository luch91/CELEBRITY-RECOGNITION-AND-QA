import base64
from flask import Blueprint, request, render_template

from app.utils.qa_engine import QnAEngine
from app.utils.celebrity_detector import CelebrityDetector
from app.utils.image_handler import process_image

main = Blueprint('main', __name__)

# Initialize the utility classes
celebrity_detector = CelebrityDetector()
qa_engine = QnAEngine()

@main.route('/', methods=['GET', 'POST'])
def index():
    player_info = ""
    result_img_data = ""
    user_question = ""
    answer = ""

    if request.method == 'POST':
        if 'image' in request.files:
            image_file = request.files['image']

            if image_file:
                img_bytes, face_box = process_image(image_file)
                player_info, player_name = celebrity_detector.identify(img_bytes)

                if face_box is not None:
                    result_img_data = base64.b64encode(img_bytes).decode()
                else:
                    player_info = "No face detected. Please try another image."

        elif "question" in request.form:
            user_question = request.form['question']
            player_name = request.form.get("player_name", "")
            player_info = request.form.get("player_info", "")
            result_img_data = request.form.get("result_img_data", "")

            answer = qa_engine.ask_about_celebrity(player_name, user_question)

    return render_template(
        'index.html',
        player_info=player_info,
        result_img_data=result_img_data,
        user_question=user_question,
        answer=answer
    )
