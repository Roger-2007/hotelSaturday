from dominio.model.User import User


class Guest(User):

    def __init__(self,id,name,last_name,phone,email,password,status,origin,occupation):
        super.__init__(id,name,last_name,phone,email,password,status)
        self._origin=origin
        self._occupation=occupation

