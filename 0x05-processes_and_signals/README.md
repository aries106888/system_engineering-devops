# 0x05. Processes and signals

## Description
This project covers the basics of Linux processes and signals. It includes tasks to manage process lifecycles, monitor running processes, and use signals to control process behavior.

## Tasks

### 0. What Is My PID?
Write a Bash script that displays its own Process ID (PID).
* File: `0-what-is-my-pid`

### 1. List Your Processes
Write a Bash script that displays a list of currently running processes with specific requirements (all processes, user-oriented format, hierarchy).
* File: `1-list_your_processes`

### 2. Show Your Bash PID
Write a Bash script that displays lines containing the word `bash` from the process list, without using `pgrep`.
* File: `2-show_your_bash_pid`

### 3. Show your Bash PID Made Easy
Write a Bash script that displays the PID and process name of processes whose name contains the word `bash`.
* File: `3-show_your_bash_pid_made_easy`

### 4. To Infinity and Beyond
Write a Bash script that displays "To infinity and beyond" indefinitely.
* File: `4-to_infinity_and_beyond`

### 5. Don't Stop Me Now!
Write a Bash script that stops the `4-to_infinity_and_beyond` process using the `kill` command.
* File: `5-dont_stop_me_now`

### 6. Stop Me if You Can
Write a Bash script that stops the `4-to_infinity_and_beyond` process without using `kill` or `killall`.
* File: `6-stop_me_if_you_can`

### 7. Highlander
Write a Bash script that displays "To infinity and beyond" indefinitely and reacts to `SIGTERM` with "I am invincible!!!".
* File: `7-highlander`

### 8. Stop Me if You Can (Highlander version)
Modify `6-stop_me_if_you_can` to kill the `7-highlander` process.
* File: `67-stop_me_if_you_can`

### 9. Beheaded Process
Write a Bash script that kills the `7-highlander` process using `SIGKILL`.
* File: `8-beheaded_process`
