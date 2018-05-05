from flask import Flask, make_response,request,send_from_directory,jsonify,render_template
import logging
from functools import wraps

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',)

app = Flask(__name__)


def log_it(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        LOGGER.info('-'*23 +"Begin")
        LOGGER.info("New Request :{}".format(request.url))
        LOGGER.info("METHOD :{}".format(request.method))
        for header in request.headers:
            LOGGER.info("{}".format(header).strip())
        if request.method not in ['GET','HEAD']:
            LOGGER.info("DATA :{}".format(request.data))
        LOGGER.info('-'*23)
        r = f(*args, **kwargs)
        LOGGER.info('-'*23 +"Completed")
        return r
    return wrapped


LOGGER = logging.getLogger("mock_svr")

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
@log_it
def index():
    return render_template(
        'index.html', data=dict(one="one",two="two"))


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
