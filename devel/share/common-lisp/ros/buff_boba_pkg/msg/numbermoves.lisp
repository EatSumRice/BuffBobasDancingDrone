; Auto-generated. Do not edit!


(cl:in-package buff_boba_pkg-msg)


;//! \htmlinclude numbermoves.msg.html

(cl:defclass <numbermoves> (roslisp-msg-protocol:ros-message)
  ((number
    :reader number
    :initarg :number
    :type cl:integer
    :initform 0))
)

(cl:defclass numbermoves (<numbermoves>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <numbermoves>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'numbermoves)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name buff_boba_pkg-msg:<numbermoves> is deprecated: use buff_boba_pkg-msg:numbermoves instead.")))

(cl:ensure-generic-function 'number-val :lambda-list '(m))
(cl:defmethod number-val ((m <numbermoves>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader buff_boba_pkg-msg:number-val is deprecated.  Use buff_boba_pkg-msg:number instead.")
  (number m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <numbermoves>) ostream)
  "Serializes a message object of type '<numbermoves>"
  (cl:let* ((signed (cl:slot-value msg 'number)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <numbermoves>) istream)
  "Deserializes a message object of type '<numbermoves>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'number) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<numbermoves>)))
  "Returns string type for a message object of type '<numbermoves>"
  "buff_boba_pkg/numbermoves")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'numbermoves)))
  "Returns string type for a message object of type 'numbermoves"
  "buff_boba_pkg/numbermoves")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<numbermoves>)))
  "Returns md5sum for a message object of type '<numbermoves>"
  "2474488a3908093ec1307bdd5b35815e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'numbermoves)))
  "Returns md5sum for a message object of type 'numbermoves"
  "2474488a3908093ec1307bdd5b35815e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<numbermoves>)))
  "Returns full string definition for message of type '<numbermoves>"
  (cl:format cl:nil "int32 number~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'numbermoves)))
  "Returns full string definition for message of type 'numbermoves"
  (cl:format cl:nil "int32 number~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <numbermoves>))
  (cl:+ 0
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <numbermoves>))
  "Converts a ROS message object to a list"
  (cl:list 'numbermoves
    (cl:cons ':number (number msg))
))
