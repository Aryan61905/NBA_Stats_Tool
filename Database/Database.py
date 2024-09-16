import sqlite3
from WebScrappers.PlayerStatsFetch import PlayerStatsFetch
from WebScrappers.ScheduleFetch import ScheduleFetch
from WebScrappers.BoxScoreFetch import BoxScoreFetch
db_ids= {
    'Main':'/Users/roy/Desktop/SPIDE/Phase3/Database/NBA_db.db',
    }
def connect_db(db_id):
    conn = sqlite3.connect(db_ids[db_id])
    cursor = conn.cursor()
    return conn, cursor

def disconnect_db(conn):
    conn.commit()
    conn.close()

def PlayersTableReset():
    createPlayersTable = '''
    CREATE TABLE PLAYERS(  
    PlayerId INTEGER PRIMARY KEY AUTOINCREMENT,
    Rk INT,  
    Player VARCHAR(150), 
    Age INT,  
    Team VARCHAR(50),  
    Pos VARCHAR(3),  
    G INT,  
    GS INT, 
    MP DOUBLE,  
    FG DOUBLE,  
    FGA DOUBLE,  
    "FG%" DOUBLE,  
    "3P" DOUBLE,  
    "3PA" DOUBLE,  
    "3P%" DOUBLE,  
    "2P" DOUBLE,  
    "2PA" DOUBLE,  
    "2P%" DOUBLE,  
    "eFG%" DOUBLE,  
    FT DOUBLE,  
    FTA DOUBLE,  
    "FT%" DOUBLE,  
    ORB DOUBLE,  
    DRB DOUBLE,  
    TRB DOUBLE,  
    AST DOUBLE,  
    STL DOUBLE,  
    BLK DOUBLE,  
    TOV DOUBLE,  
    PF DOUBLE,  
    PTS DOUBLE,  
    Awards VARCHAR(255)); 
    '''

    conn,cursor = connect_db("Main")
    cursor.execute('DROP TABLE IF EXISTS PLAYERS')
    cursor.execute(createPlayersTable)
    disconnect_db(conn)

def PlayersTableUpdate():
    PlayersTableReset()
    player_data = PlayerStatsFetch()[1:-1]
    player_val = ''
    for pd in player_data:
        player_val+= f"(null,{str(pd)[1:-1]}), "

    updatePlayersTable = f'''
    INSERT INTO PLAYERS (PlayerId, Rk, Player, Age, Team, Pos, G, GS, MP, FG, FGA, `FG%`, `3P`, `3PA`, `3P%`, `2P`, `2PA`, `2P%`, `eFG%`, FT, FTA, `FT%`, ORB, DRB, TRB, AST, STL, BLK, TOV, PF, PTS, Awards)
    VALUES {player_val[:-2]};'''
    conn,cursor = connect_db("Main")
    cursor.execute(updatePlayersTable)
    disconnect_db(conn)

def ScheduleTableReset():
    createScheduleTable = '''
    CREATE TABLE SCHEDULE( 
    ScheduleId INTEGER PRIMARY KEY AUTOINCREMENT, 
    Date VARCHAR(10), 
    StartTime VARCHAR(5), 
    AwayTeam VARCHAR(3), 
    AwayTeamPTS INT, 
    HomeTeam VARCHAR(3), 
    HomeTeamPTS INT, 
    BoxScoreId VARCHAR(100), 
    OverTime VARCHAR(3), 
    Attendence VARCHAR(6), 
    LengthOfGame VARCHAR(4), 
    Arena VARCHAR(50), 
    Notes VARCHAR(100)
    ); 
    '''

    conn,cursor = connect_db("Main")
    cursor.execute('DROP TABLE IF EXISTS SCHEDULE')
    cursor.execute(createScheduleTable)
    disconnect_db(conn)

def ScheduleTableUpdate():
    ScheduleTableReset()
    schedule_data = ScheduleFetch()
    schedule_val = ''
    for sd in schedule_data:
        schedule_val+= f"(null,{str(sd)[1:-1]}), "

    updateScheduleTable = f'''
    INSERT INTO SCHEDULE (ScheduleId, Date, StartTime, AwayTeam, AwayTeamPTS, HomeTeam, HomeTeamPTS, BoxScoreId, OverTime, Attendence, LengthOfGame, Arena, Notes)
    VALUES {schedule_val[:-2]};'''
    conn,cursor = connect_db("Main")
    cursor.execute(updateScheduleTable)
    disconnect_db(conn)

def BoxScoreTableReset():
    createBoxScoreBasicTable = '''
    CREATE TABLE BoxScoreBasic( 
    BoxScoreID INTEGER PRIMARY KEY AUTOINCREMENT, 
    Player, 
    MP, 
    FG, 
    FGA, 
    "FG%", 
    "3P", 
    "3PA", 
    "3P%", 
    FT, 
    FTA, 
    "FT%", 
    ORB, 
    DRB, 
    TRB, 
    AST, 
    STL, 
    BLK, 
    TOV, 
    PF, 
    PTS, 
    GmSc, 
    "+/-",
    BenchStatus,
    Team,
    Opponent,
    Type
    ); 
    '''

    createBoxScoreAdvancedTable = '''
    CREATE TABLE BoxScoreBasic( 
    BoxScoreID INTEGER PRIMARY KEY AUTOINCREMENT, 
    Player, 
    MP, 
    "TS%", 
    "eFG%", 
    "3PAr", 
    FTr, 
    "ORB%", 
    "DRB%", 
    "TRB%", 
    "AST%", 
    "STL%", 
    "BLK%", 
    "TOV%", 
    "USG%", 
    ORtg, 
    DRtg, 
    BPM,
    BenchStatus,
    Team,
    Opponent,
    Type
   ); 
    '''

    conn,cursor = connect_db("Main")
    cursor.execute('DROP TABLE IF EXISTS SCHEDULE')
    cursor.execute(createBoxScoreAdvancedTable)
    disconnect_db(conn)
   



#PlayersTableUpdate()
#ScheduleTableUpdate()
