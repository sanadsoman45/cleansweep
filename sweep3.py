from gevent.pywsgi import WSGIServer
from werkzeug.debug import DebuggedApplication
from flask import Flask
from flask import render_template,request,url_for,redirect
import RPi.GPIO as gp
import time
from OpenSSL import SSL
'''context = SSL.Context(SSL.proto)
context.use_privatekey_file('server.key')
context.use_certificate_file('server.crt')
'''

try:
        print("in try")
        in1=16
        in2=18
        in3=11
        in4=13
        pmp=7
        gp.setmode(gp.BOARD)
        #gp.setup(22,gp.OUT)
        #gp.setup(7,gp.OUT)
        gp.setup(in1,gp.OUT)
        gp.setup(in2,gp.OUT)
        gp.setup(in3,gp.OUT)
        gp.setup(in4,gp.OUT)
        gp.setup(pmp,gp.OUT)
        gp.output(in1,False)
        gp.output(in2,False)
        gp.output(in3,False)
        gp.output(in4,False)
        gp.output(pmp,False)
        #gp.setup(21,gp.OUT)
        #gp.output(21,True)
        #en1=gp.PWM(22,100)
        #en2=gp.PWM(7,100)
        app = Flask(__name__)
        @app.route("/")
        def index():
            return render_template('sweep2.html') 
        @app.route('/right')
        def left():
            gp.output(in1,False)
            gp.output(in2,False)
            gp.output(in3,False)
            gp.output(in4,False)
            #en1.start(80)
            #en2.start(60)
            #gp.output(in1,True)
            #gp.output(in2,False)
            #gp.output(in3,True)
            gp.output(in3,True)
            #time.sleep(8.5)
            #gp.cleanup()
            return "True"
        @app.route('/left')
        def right():
            gp.output(in1,False)
            gp.output(in2,False)
            gp.output(in3,False)
            gp.output(in4,False)
            #en1.start(80)
            #en2.start(60)
            #gp.output(in1,False)
            #gp.output(in2,True)
            gp.output(in1,True)
            #gp.output(in4,False)
            #time.sleep(17.5)
           # gp.cleanup()
            return "True"
        @app.route('/forward')
        def forward():
            print("running forward")
            gp.output(in1,False)
            gp.output(in2,False)
            gp.output(in3,False)
            gp.output(in4,False)
            #en1.start(70)
            #en2.start(100)
           # gp.output(in1,True)
            gp.output(in1,True)
            #gp.output(in2,False)
            gp.output(in3,True)
            #gp.output(in4,False)
            #gp.cleanup()
            return "True"

        @app.route('/backward')
        def backward():
            print("running backward")
            gp.output(in1,False)
            gp.output(in2,False)
            gp.output(in3,False)
            gp.output(in4,False)
            #en1.start(90) 
            #en2.start(100)
            #gp.cleanup()
            #gp.output(in1,True)
            gp.output(in2,True)
            #gp.output(in3,False)
            gp.output(in4,True)
            return "True"
        @app.route('/pump')
        def pump():
                gp.output(pmp,True)
                return "True"
        @app.route('/stop')
        def stop():
                gp.output(in1,False)
                gp.output(in2,False)
                gp.output(in3,False)
                gp.output(in4,False)
                gp.output(pmp,False)
                return "True"
        @app.route('/voice')
        def voice():
                cmd=request.args.get('command')
                print(cmd)
                if(cmd!=None):
                        if(cmd)=="forward":
                                print("running forward")
                                gp.output(in1,False)
                                gp.output(in2,False)
                                gp.output(in3,False)
                                gp.output(in4,False)
                                gp.output(in1,True)
                                gp.output(in3,True)
                                cmd=None
                        elif(cmd)=="backward":
                                print("running backward")
                                gp.output(in1,False)
                                gp.output(in2,False)
                                gp.output(in3,False)
                                gp.output(in4,False)
                                gp.output(in2,True)
                                gp.output(in4,True)
                                cmd=None
                        elif(cmd)=="left":
                                print("running left")
                                gp.output(in1,False)
                                gp.output(in2,False)
                                gp.output(in3,False)
                                gp.output(in4,False)
                                gp.output(in1,True)
                                cmd=None
                        elif(cmd)=="right":
                                print("running right")
                                gp.output(in1,False)
                                gp.output(in2,False)
                                gp.output(in3,False)
                                gp.output(in4,False)
                                gp.output(in3,True)
                                cmd=None
                        elif(cmd)=="pump":
                                print("pump on")
                                gp.output(pmp,True)
                                time.sleep(1)
                                gp.output(pmp,False)
                                cmd=None
                        
                #return render_template('sweep2.html')
                return redirect(url_for('index'))
                                        
                
        if __name__ == "__main__":
                        print ("Start")
                        app.run(host='192.168.0.6',port=5020,threaded=True,ssl_context='adhoc')
                        #WSGIServer(('192.168.0.6',5020),app).serve_forever()
finally:
	print("in finally")
	gp.cleanup()

