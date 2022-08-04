
(cl:in-package :asdf)

(defsystem "buff_pkg-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Moves" :depends-on ("_package_Moves"))
    (:file "_package_Moves" :depends-on ("_package"))
    (:file "Song" :depends-on ("_package_Song"))
    (:file "_package_Song" :depends-on ("_package"))
    (:file "State" :depends-on ("_package_State"))
    (:file "_package_State" :depends-on ("_package"))
  ))