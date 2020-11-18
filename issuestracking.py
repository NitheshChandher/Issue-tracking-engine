import random
import datetime
from datetime import datetime, timedelta
issues={} # dictionary with IssueIDs as keys and the issues, startdate and enddate as values
users={} # dictionary with UserIDs as keys and the user names as values
states={} # dictionary with IssueIDs as keys and the state of the issue as values
comments={} # dictionary with IssueIDs as keys and the comments for the issues as values
assigntask={} # dictionary with IssueIDs as keys and the UserIDs assigned to the issues as values

#Function to add issue
def addIssue(title):
  issueID = random.randint(1,100)
  startdate = None
  enddate = None
  if issueID < 50:   #Assigning start date and end date only for issueIDs less than 50 (for randomness)
    startdate = datetime.now()
    td = timedelta(days=random.randint(1,10))
    enddate = startdate + td
    startdate = startdate.strftime("%d/%m/%Y")
    enddate = enddate.strftime("%d/%m/%Y")
  issues[issueID] = [title,startdate,enddate] #date format "%d/%m/%Y"
  return issueID

#Function to remove Issue
def removeIssue(issueID):
  del issues[issueID]

#Function to set issue state
def setIssueState(issueID, state, comment = None):
  states[issueID] = state
  comments[issueID] = comment 

#Function to assign user to issue
def assignUser(issueID,userID):
  assigntask[issueID] = userID

#Function to add issue comment
def addIssueComment(issueID,comment):
  comments[issueID] = comment 

#Function to check date condition in getIssues()
def datecondition(startDate,endDate,allissues,ls):  
      
  if startDate !=None and endDate != None:
    for j in ls:
      sdate = issues[j][1]
      edate = issues[j][2]
      if sdate != None and edate != None:
        if sdate>= startDate and edate < endDate:
          allissues.append(list(issues[j]))


  if startDate != None:
    for j in ls:
      date = issues[j][1]
      if date != None:
        if date >= startDate:
          allissues.append(list(issues[j]))

  if endDate != None:
    for j in ls:
      date = issues[j][2]
      if date != None:
        if date < endDate:
          allissues.append(list(issues[j]))
 
  return allissues

# Function to get list of issues
def getIssues(state = None, userID = None, startDate = None, endDate = None):
  ls=[]
  allissues=[]

  if state != None:
    ls.append(list(states.keys())[list(states.values()).index(str(state))])
    for j in ls:
      allissues.append(list(issues[j]))
    allissues = datecondition(startDate,endDate,allissues,ls)
  
  if userID != None:
    ls.append(list(assigntask.keys())[list(assigntask.values()).index(userID)])
    for j in ls:
      allissues.append(list(issues[j]))
    allissues = datecondition(startDate,endDate,allissues,ls)
  
  if (userID == None and state == None) and (startDate != None or endDate != None):
    allissues = datecondition(startDate,endDate,allissues,issues.keys())
  
  if state == None and userID == None and startDate == None and endDate == None:
    for j in range(0,len(issues)):
      allissues.append(list(issues.values())[j])
  #output of the form [Issue, Start Date, End Date]
  return [list(tupl) for tupl in {tuple(item) for item in allissues }]   #removes duplicate

#Function to get specific issue
def getIssue(issueID):
  issue = issues[issueID]
  return issue

#Function to add user
def addUser(name):
  userID = random.randint(101,200)
  users[userID] = name
  return userID

#Function to remove user
def removeUser(userID):
  del users[userID]

#Function to get list of users
def getUsers():
  return users.values()

#Function to get specific user
def getUser(userID):
  user = users[userID]
  return user

def display():
  print('Issues created: ',issues)
  print('\nUsers created: ',users)
  print('\nIssues assigned to users: ',assigntask)
  print('\nStates of each issues: ',states)
  print('\nComments given to each issues: ',comments)

#test function
def testScenario1():
  userID = addUser("Steve")
  issueID = addIssue("The app crashes on login.")
  assignUser(userID, issueID)
  setIssueState(issueID, 'IN_PROGRESS_STATE', "I'm on it!")

testScenario1()
display()