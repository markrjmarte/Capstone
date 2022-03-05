import sqlite3
conn = sqlite3.connect('data.db',check_same_thread=False)
c = conn.cursor()


def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS dtast(Id TEXT,Fname TEXT,Mname TEXT,Lname TEXT, AcYear TEXT,Course TEXT,Gender TEXT,Address TEXT,bdate DATE,bplace TEXT,Religion TEXT,Cnumber TEXT,CStatus TEXT,Eacc TEXT, ActiveStatus TEXT,message TEXT,response TEXT,res_status Text)')


def add_data(Id,Fname ,Mname ,Lname ,AcYear ,Course ,Gender ,Address ,bdate ,bplace,Religion ,Cnumber ,CStatus ,Eacc,ActiveStatus,message,response,res_status):
	c.execute('INSERT INTO dtast(Id ,Fname ,Mname ,Lname ,AcYear ,Course ,Gender ,Address ,bdate ,bplace,Religion ,Cnumber ,CStatus ,Eacc,ActiveStatus,message,response,res_status) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(Id ,Fname ,Mname ,Lname ,AcYear ,Course ,Gender ,Address ,bdate ,bplace,Religion ,Cnumber ,CStatus ,Eacc,ActiveStatus,message,response,res_status))
	conn.commit()

def login_user(Id,Lname):
    c.execute('SELECT * FROM dtast WHERE Id=? AND Lname=?',(Id,Lname))
    data = c.fetchall()
    return data

def active_status(new_ActiveStatus,ActiveStatus,Id):
    c.execute('UPDATE dtast SET ActiveStatus =? WHERE ActiveStatus =? AND Id =?',(new_ActiveStatus,ActiveStatus,Id))
    conn.commit()
    data = c.fetchall()
    return data
    
def view_all_data():
	c.execute('SELECT Id,Fname ,Mname ,Lname ,AcYear ,Course ,Gender ,Address ,bdate ,bplace,Religion ,Cnumber ,CStatus ,Eacc FROM dtast')
	data = c.fetchall()
	return data

def onlinestatus():
    c.execute('SELECT ActiveStatus,Id,Fname ,Mname ,Lname ,AcYear ,Course FROM dtast WHERE ActiveStatus="Online"')
    data = c.fetchall()
    return data

def get_status_Admin_user(Id):
    c.execute('SELECT DISTINCT ActiveStatus FROM dtast WHERE Id="{}"'.format(Id))
    data = c.fetchall()
    return data

def view_all_StudentId():
	c.execute('SELECT DISTINCT Id FROM dtast')
	data = c.fetchall()
	return data

def view_all_StudentFname():
	c.execute('SELECT DISTINCT Fname FROM dtast')
	data = c.fetchall()
	return data
    
def get_Id(Id):
	c.execute('SELECT * FROM dtast WHERE Id="{}"'.format(Id))
	data = c.fetchall()
	return data

def edit_Fname_data(new_Id ,new_Fname,new_Mname,new_Lname,new_AcYear ,new_Course ,new_Gender ,new_Address ,new_bdate ,new_bplace,new_Religion ,new_Cnumber ,new_CStatus ,new_Eacc,Id ,Fname ,Mname ,Lname ,AcYear ,Course ,Gender ,Address ,bdate ,bplace,Religion ,Cnumber ,CStatus ,Eacc):
	c.execute("UPDATE dtast SET Id =?,Fname =?,Mname =?,Lname=? ,AcYear =? ,Course =?,Gender =?,Address =?,bdate =?,bplace =?,Religion =?,Cnumber =?,CStatus =? ,Eacc =? WHERE Id =? and Fname =? and Mname =? and Lname =? and AcYear=?  and Course=? and Gender =? and Address =? and bdate =? and bplace=? and Religion =? and Cnumber =? and CStatus =?  and Eacc =?",(new_Id ,new_Fname,new_Mname,new_Lname,new_AcYear ,new_Course ,new_Gender ,new_Address ,new_bdate ,new_bplace,new_Religion ,new_Cnumber ,new_CStatus ,new_Eacc,Id ,Fname ,Mname ,Lname ,AcYear ,Course ,Gender ,Address ,bdate ,bplace,Religion ,Cnumber ,CStatus ,Eacc))
	conn.commit()
	data = c.fetchall()
	return data

def view_update_convo(new_message,Id,message):
    c.execute("UPDATE dtast SET message=? WHERE Id=? AND message=? ",(new_message,Id,message))
    conn.commit()
    data=c.fetchall()
    return data

def update_convo_r(new_response,Id,response):
    c.execute("UPDATE dtast SET response=? WHERE Id=? AND response=?",(new_response,Id,response))
    conn.commit()
    data=c.fetchall()
    return data

def convo_save():
    c.execute('SELECT Id,Fname,Mname ,Lname ,AcYear ,Course,message,response FROM dtast')
    data=c.fetchall()
    return data

    
def view_datattodelete(Id):
	c.execute('SELECT * FROM dtast WHERE Id="{}"'.format(Id))
	data = c.fetchall()
	return data
    
def delete_data(Id):
	c.execute('DELETE FROM dtast WHERE Id="{}"'.format(Id))
	conn.commit()
    
def response_status():
    c.execute('SELECT Id, Fname,Mname, Lname, AcYear, Course,message, response FROM dtast WHERE res_status ="Not ok" And response ="None" AND message != "None"')
    data=c.fetchall()
    return data

def response_status_change(new_rStatus,res_status,Id):
    c.execute('UPDATE dtast SET res_status =? WHERE res_status =? AND Id =?',(new_rStatus,res_status,Id))
    conn.commit()
    data = c.fetchall()
    return data