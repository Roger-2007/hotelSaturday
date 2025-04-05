from dominio.model.User import User

class Worker(User):
    def __init__(self, id, name, last_name, phone, email, password, status, salary, job):
        #super.__init__(id,name,last_name,phone,email,password,status)
        super().__init__(id, name, last_name, phone, email, password, status)
        self._salary=salary
        self._job=job

    #@property
    def get_salary(self):
        return self._salary
    def set_salary(self,salary):
        self._salary=salary
    def get_job(self):
        return self._job
    def set_job(self,job):
        self._job=job