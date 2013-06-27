import logging

logger = logging.getLogger('flask_upstatic')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

from flask import Flask, render_template
from flask_upstatic import Upstatic


if __name__ == '__main__':
  app = Flask(__name__)
  app.config.update(
    UPSTATIC_S3_ACCESS_KEY_ID=raw_input('S3 Access Key ID: '),
    UPSTATIC_S3_SECRET_ACCESS_KEY=raw_input('S3 Secret Access Key: '),
    UPSTATIC_S3_BUCKET_NAME='flask_upstatic',
  )
  upstatic = Upstatic(app)
  upstatic.add_root('home', 'static')

  upstatic.upload_all('home')

  app.add_template_global(upstatic.url_for)

  @app.route('/')
  def index():
    return render_template('index.html')

  app.run()

