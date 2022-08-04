;; Auto-generated. Do not edit!


(when (boundp 'buff_boba_pkg::numbermoves)
  (if (not (find-package "BUFF_BOBA_PKG"))
    (make-package "BUFF_BOBA_PKG"))
  (shadow 'numbermoves (find-package "BUFF_BOBA_PKG")))
(unless (find-package "BUFF_BOBA_PKG::NUMBERMOVES")
  (make-package "BUFF_BOBA_PKG::NUMBERMOVES"))

(in-package "ROS")
;;//! \htmlinclude numbermoves.msg.html


(defclass buff_boba_pkg::numbermoves
  :super ros::object
  :slots (_number ))

(defmethod buff_boba_pkg::numbermoves
  (:init
   (&key
    ((:number __number) 0)
    )
   (send-super :init)
   (setq _number (round __number))
   self)
  (:number
   (&optional __number)
   (if __number (setq _number __number)) _number)
  (:serialization-length
   ()
   (+
    ;; int32 _number
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _number
       (write-long _number s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _number
     (setq _number (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get buff_boba_pkg::numbermoves :md5sum-) "2474488a3908093ec1307bdd5b35815e")
(setf (get buff_boba_pkg::numbermoves :datatype-) "buff_boba_pkg/numbermoves")
(setf (get buff_boba_pkg::numbermoves :definition-)
      "int32 number
")



(provide :buff_boba_pkg/numbermoves "2474488a3908093ec1307bdd5b35815e")


