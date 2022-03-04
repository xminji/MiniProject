from flask import Flask, render_template
import routes.infection_route as irt
import routes.cc_route as cr
import d0208_project_mini00.routes.hosp_route as hr
import d0208_project_mini00.routes.status_route as sr



app = Flask(__name__)


app.register_blueprint(irt.bp)
app.register_blueprint(cr.bp)
app.register_blueprint(hr.bp)
app.register_blueprint(sr.bp)


@app.route('/')
def root():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
    # db.run()
    # migrate.run()