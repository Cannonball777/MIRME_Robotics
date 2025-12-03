#!/usr/bin/env python3


import rclpy #librería principal de ROS 2
from rclpy.node import Node #Se importa la clase Node para crear nodos
from std_msgs.msg import Float64

import time
from math import cos, sin, acos, asin, atan2, sqrt #para las ecuaciones trigonométricas de la cinemática inversa

class ScaraTrayLineNode(Node): 
    def __init__(self):
        super().__init__("scara_tray_line_node") #nombre del nodo
        
        topic_link_joint1 = "/joint1/cmd_pos"
        topic_link_joint2 = "/joint2/cmd_pos"
        topic_link_joint3 = "/joint3/cmd_pos"
        
        self.pubj1_ = self.create_publisher(Float64, topic_link_joint1, 10)
        self.pubj2_ = self.create_publisher(Float64, topic_link_joint2, 10)
        self.pubj3_ = self.create_publisher(Float64, topic_link_joint3, 10)

        self.lamda_ = 0 #Trayectoria        
        self.timer_ = self.create_timer(1.0, self.tray_callback) #la variable self.tray_timer_ hace que la función trayectory_cvck se ejecute cada segundo
        self.get_logger().info('Nodo de trayectoria activado') #arroja un mensaje en la terminal indicando que el nodo está activo

    def tray_callback(self): #se define la función trayectory_cbck
        #Mientras la trayectoria no termine
        if self.lamda_ <= 8:
            temp = 8 #Tiempo para la ejecución de la trayectoria
            x_1 = 0.25
            y_1 = 0.8
            theta_1 = 1.27 #se define la posición del punto inicial P1
            x_2 = 0.25
            y_2 = 1.05
            theta_2 = 1.337 #se define la posición del punto final P2
            solucion = invk_sol(self.lamda_, x_1, y_1,theta_1, x_2, y_2,theta_2,temp) #se invoca la función invk_sol que resuelve la trayectoria
            # Se declaran las variables de mensaje
            msg1 = Float64()
            msg2 = Float64()
            msg3 = Float64()

            msg1.data = solucion[0]
            msg2.data = solucion[1]
            msg3.data = solucion[2]

            self.pubj1_.publish(msg1)
            self.pubj2_.publish(msg2)
            self.pubj3_.publish(msg3)

            self.get_logger().info("Postura actual {}".format(solucion)) #muestra un mensaje en la terminal que indica las posiciones actuales de los ángulos
            time.sleep(2) #pausa 2 segundos para simular el paso del tiempo
            self.lamda_ += 1 #incrementa el valor de lamda que determina el progreso de la trayectoria
        elif 8 < self.lamda_ <= 23:
            temp = 15
            x_1 = 0.25
            y_1 = 1.05
            theta_1 = 1.337
            x_2 = -0.25
            y_2 = 1.05
            theta_2 = -1.337
            solucion = invk_sol(self.lamda_, x_1, y_1, theta_1, x_2, y_2, theta_2,temp)
            # Se declaran las variables de mensaje
            msg1 = Float64()
            msg2 = Float64()
            msg3 = Float64()

            msg1.data = solucion[0]
            msg2.data = solucion[1]
            msg3.data = solucion[2]

            self.pubj1_.publish(msg1)
            self.pubj2_.publish(msg2)
            self.pubj3_.publish(msg3)
            
            self.get_logger().info("Postura actual {}".format(solucion))
            time.sleep(2)
            self.lamda_ += 1
        elif 23 < self.lamda_ <= 38:
            temp = 15
            x_1 = -0.25
            y_1 = 1.05
            theta_1 = -1.337
            x_2 = -0.25
            y_2 = 0.55
            theta_2 = -1.144
            solucion = invk_sol(self.lamda_, x_1, y_1, theta_1, x_2, y_2, theta_2,temp)
            # Se declaran las variables de mensaje
            msg1 = Float64()
            msg2 = Float64()
            msg3 = Float64()

            msg1.data = solucion[0]
            msg2.data = solucion[1]
            msg3.data = solucion[2]

            self.pubj1_.publish(msg1)
            self.pubj2_.publish(msg2)
            self.pubj3_.publish(msg3)

            self.get_logger().info("Postura actual {}".format(solucion))
            time.sleep(2)
            self.lamda_ += 1
        elif 38 < self.lamda_ <= 53:
            temp = 15
            x_1 = -0.25
            y_1 = 0.55
            theta_1 = -1.144
            x_2 = 0.25
            y_2 = 0.55
            theta_2 = 1.144
            solucion = invk_sol(self.lamda_, x_1, y_1, theta_1, x_2, y_2, theta_2,temp)
            # Se declaran las variables de mensaje
            msg1 = Float64()
            msg2 = Float64()
            msg3 = Float64()

            msg1.data = solucion[0]
            msg2.data = solucion[1]
            msg3.data = solucion[2]

            self.pubj1_.publish(msg1)
            self.pubj2_.publish(msg2)
            self.pubj3_.publish(msg3)

            self.get_logger().info("Postura actual {}".format(solucion))
            time.sleep(2)
            self.lamda_ += 1
        elif 53 < self.lamda_ <= 61:
            temp = 8
            x_1 = 0.25
            y_1 = 0.55
            theta_1 = 1.144
            x_2 = 0.25
            y_2 = 0.8
            theta_2 = 1.27
            solucion = invk_sol(self.lamda_, x_1, y_1, theta_1, x_2, y_2, theta_2,temp)
            # Se declaran las variables de mensaje
            msg1 = Float64()
            msg2 = Float64()
            msg3 = Float64()

            msg1.data = solucion[0]
            msg2.data = solucion[1]
            msg3.data = solucion[2]

            self.pubj1_.publish(msg1)
            self.pubj2_.publish(msg2)
            self.pubj3_.publish(msg3)

            self.get_logger().info("Postura actual {}".format(solucion))
            time.sleep(2)
            self.lamda_ += 1
        elif self.lamda_ > 61: #si lambda alcanza un valor mayor al tiempo de ejecución...
            msg1 = Float64()
            msg2 = Float64()
            msg3 = Float64()

            msg1.data = 0.0
            msg2.data = 0.0
            msg3.data = 0.0

            self.pubj1_.publish(msg1)
            self.pubj2_.publish(msg2)
            self.pubj3_.publish(msg3)
            self.destroy_timer(self.timer_)

def invk_sol(param,x_in, y_in, theta_in, x_fin, y_fin, theta_fin,t): #la función invk_sol tiene como parámetros los valores de la posición inicial y final, es la función que resuelve la cinemática
    Tiempo_ejec_ = t #se ajusta el tiempo de ejecución dependiendo el valor de t [segundos]
    L_1 = 0.5
    L_2 = 0.5
    L_3 = 0.2 #se definen las longitudes de los eslabones del robot SCARA
    x_P = x_in + (param/Tiempo_ejec_)*(x_fin - x_in)
    y_P = y_in + (param/Tiempo_ejec_)*(y_fin - y_in)
    theta_P = theta_in + (param/Tiempo_ejec_)*(theta_fin - theta_in) #para estos 3 valores del punto P se calcula un incremento lineal en el rango inicial y final que depende del aumento de lamda
    x_3 = x_P - L_3*cos(theta_P) #calcula la abscisa de la junta 3 en el sistema inercial
    y_3 = y_P - L_3*sin(theta_P) #calcula la ordenada de la junta 3 en el sistema inercial

    arg1 = (pow(x_3, 2)+pow(y_3,2)-pow(L_1, 2)-pow(L_2, 2))/(2*L_1*L_2)
    arg1 = max(min(arg1,1),-1) #el argumento del coseno se limita para evitar errores numéricos
    theta_2 = acos(arg1) #se utiliza ley de cosenos para determinar el ángulo del eslabón 2, en clase se proponía ley de senos

    beta = atan2(y_3, x_3) #en clase este ángulo fue llamado Epsilon y se encuentra entre P_0_1_3 y x_0; donde P_0_1_3 es el vector de posición del efector final que apunta del origen a la junta 3

    arg2 = (pow(x_3, 2)+pow(y_3,2)+pow(L_1, 2)-pow(L_2, 2))/(2*L_1*sqrt(pow(x_3, 2)+pow(y_3,2)))
    arg2 = max(min(arg2,1),-1)
    psi = acos(arg2) #en clase este ángulo fue llamado alfa y se encuentra entre el eslabón l1 y P_0_1_3
    theta_1 = beta - psi #gracias a los ángulos calculados anteriormente se puede obtener el ángulo del eslabón 1
    theta_3 = theta_P -theta_1 -theta_2 #se calcula el ángulo del efector final (del eslabón 3)
    return [float(theta_1), float(theta_2), float(theta_3)] #devuelve los valores de los 3 ángulos calculados

def main(args=None): #Inicializa el entorno de ROS 2 y ejecuta el nodo ScaraTrayLineNode()
    rclpy.init(args=args)
    node = ScaraTrayLineNode()
    rclpy.spin(node) #mantiene el nodo activo
    rclpy.shutdown() #permite cerrar ROS 2 y terminar

if __name__ == "__main__": #Llamada directa para ejecutar el nodo
    main()