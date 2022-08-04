; Auto-generated. Do not edit!


(cl:in-package buff_pkg-msg)


;//! \htmlinclude Moves.msg.html

(cl:defclass <Moves> (roslisp-msg-protocol:ros-message)
  ((moveList
    :reader moveList
    :initarg :moveList
    :type cl:string
    :initform ""))
)

(cl:defclass Moves (<Moves>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Moves>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Moves)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name buff_pkg-msg:<Moves> is deprecated: use buff_pkg-msg:Moves instead.")))

(cl:ensure-generic-function 'moveList-val :lambda-list '(m))
(cl:defmethod moveList-val ((m <Moves>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader buff_pkg-msg:moveList-val is deprecated.  Use buff_pkg-msg:moveList instead.")
  (moveList m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Moves>) ostream)
  "Serializes a message object of type '<Moves>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'moveList))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'moveList))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Moves>) istream)
  "Deserializes a message object of type '<Moves>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'moveList) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'moveList) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Moves>)))
  "Returns string type for a message object of type '<Moves>"
  "buff_pkg/Moves")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Moves)))
  "Returns string type for a message object of type 'Moves"
  "buff_pkg/Moves")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Moves>)))
  "Returns md5sum for a message object of type '<Moves>"
  "4697aa5897206b11660bd043405f4a49")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Moves)))
  "Returns md5sum for a message object of type 'Moves"
  "4697aa5897206b11660bd043405f4a49")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Moves>)))
  "Returns full string definition for message of type '<Moves>"
  (cl:format cl:nil "string moveList~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Moves)))
  "Returns full string definition for message of type 'Moves"
  (cl:format cl:nil "string moveList~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Moves>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'moveList))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Moves>))
  "Converts a ROS message object to a list"
  (cl:list 'Moves
    (cl:cons ':moveList (moveList msg))
))
