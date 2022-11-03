import tkinter as tk
from tkinter import ttk
import MaxPreps_TeamScorer_v1 as teamscorer

root = tk.Tk()
root.title('TeamScorer Web Scraping Interface')

#create label with text "MaxPreps TeamScorer"
#center it in column 0, row 0 with columnspan == 2
title_label = ttk.Label(root, text = 'MaxPreps TeamScorer')
title_label.grid(column = 0, row = 0, columnspan = 2)

#create label with text "Team Name:"
#grid in column 0, row 1
#create entry in column 1, row 1
team_name_label = ttk.Label(root, text = 'Team Name: ')
team_name_label.grid(column = 0, row = 1)

team_name_value = tk.StringVar()
team_name_entry = ttk.Entry(root, textvariable = team_name_value)
team_name_entry.grid(column = 1, row = 1)

#create label with text "City:"
#grid it in column 0, row 2
#grid an entry in column 1, row 2
city_label = ttk.Label(root, text = 'City: ')
city_label.grid(column = 0, row = 2)

city_name_value = tk.StringVar()
city_entry = ttk.Entry(root, textvariable = city_name_value)
city_entry.grid(column = 1, row = 2)

#create label with text "State Abbreviation: "
#grid it in column 0, row 3
#grid a OptionMenu in column 1, row 3
state_abbrv_label = ttk.Label(root, text = 'State Abbreviation: ')
state_abbrv_label.grid(column = 0, row = 3)
list_of_options = ['il', 2, 3, 'hi', 'bye']
state_abbrv_value = tk.StringVar()
state_abbrv_OptionMenu = tk.OptionMenu(root, state_abbrv_value, *list_of_options)
state_abbrv_OptionMenu.grid(column = 1, row = 3)

#create a label with text "Year: "
#grid it in column 0, row 4
#grid an OptionMenu in column 1, row 4
year_label = ttk.Label(root, text = 'Year: ')
year_label.grid(column = 0, row = 4)
year_value = tk.StringVar()
year_options = ['19-20', '20-21', '21-22']
year_OptionMenu = tk.OptionMenu(root, year_value, *year_options)
year_OptionMenu.grid(column = 1, row = 4)

#create a button with text "GO"
#grid it in column 0, row 5 with columnspan == 2
#center it in row 5
#add functionality that opens a new TopLevel when user clicks button
def open_new_window():
    # should open upon click of "GO" button in row 5
    results_window = tk.Toplevel(root)
    results_window.title('worked?')

    # create label with text "TeamScorer Results"
    # grid it in column 0, row 0 with columnspan 4
    teamscorer_results_label = ttk.Label(results_window, text = 'TeamScorer Results')
    teamscorer_results_label.grid(column = 0, row = 0, columnspan = 4)

    # create label with text "Average Opponent Winrate: {textvar}"
    # grid it in column 0, row 1
    # link textvar to calculation from teamscorer file
    #create entry in column 1, row 1
    average_opp_winrate_value = 'temp'
    average_opp_winrate_label = ttk.Label(results_window, text = 'Average Opponent Winrate: ')
    average_opp_winrate_entry = ttk.Entry(results_window, textvariable = average_opp_winrate_value)
    average_opp_winrate_label.grid(column = 0, row = 1)
    average_opp_winrate_entry.grid(column = 1, row = 1)

    # create label with text "Average Opponent Games Played: {textvar}"
    # grid it in column 2, row 1
    # create entry in column 3, row 1
    # link textvar to calculation from teamscorer file(diff calc from winrate)
    avg_opp_games_played_value = 'temp'
    avg_opp_games_played_label = ttk.Label(results_window, text ='Average Opponent Games Played: ')
    avg_opp_games_played_entry = ttk.Entry(results_window, textvariable = avg_opp_games_played_value)
    avg_opp_games_played_label.grid(column = 2, row = 1)
    avg_opp_games_played_entry.grid(column = 3, row = 1)

    # create label with text "Home Team's Winrate: {Text Var}"
    # grid it in column 0, row 2
    # grid entry in column 1, row 2
    # link textvar to variable from teamscorer file

    # create label with text "Average Opponent's StrengthScore: {textvar}"
    # ADDIT FEAT: add hover over pop up on StrengthScore
    # grid this in column 2, row 2
    # grid entry in column 3, row 2
    # link textvar to calculation from teamscorer file

    # create label with text "Overall Team Rating"
    # grid this in column 0, row 3 with columnspan of 4

    # create label with text "{textvar}"
    # add color/effect to this label text(maybe change font)
    # grid this in column 0, row 4 with columnspan of 4

    # create label with text "Try Another Team?"
    # grid this in column 0, row 5
    # create a button with text "Back to Home Page"
    # grid this in column 2, row 5(directly next to label)

    # create label with text "Thanks for using TeamScorer"
    # grid this in column 0, row 6 with columnspan 4
    # although centered in two columns, make text smaller
    return 1

go_button = ttk.Button(root, text = 'GO', command = open_new_window)
go_button.grid(column = 0, row = 5, columnspan = 2)


misc_frame = ttk.Frame(root)
misc_frame.grid(column = 0, row = 6, columnspan = 2)

conditions_label = ttk.Label(misc_frame, text = 'Terms and Conditions')
conditions_label.grid(row = 0, column = 0)

logo_label = ttk.Label(misc_frame, text = 'TEMP') #will have an image in future
logo_label.grid(row = 0, column = 1)

teamscorer_info_label = ttk.Label(misc_frame, text = 'How Does TeamScorer Work?')
teamscorer_info_label.grid(row = 0, column = 2)


for children in root.winfo_children():
    children.grid_configure(padx = 2.5, pady = 5)

tk.mainloop()
# print(team_name_value.get())
# print(city_name_value.get())
# print(state_abbrv_value.get())
# print(year_value.get())