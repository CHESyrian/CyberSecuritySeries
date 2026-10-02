# 04 — Command Line in Depth

## Introduction

The shell is the primary interface for serious Linux work. This module goes beyond basic navigation and explains how the shell parses commands, expands words, handles input/output, manages jobs, and exposes the environment. It also covers a practical set of tools that appear constantly in security and system-administration work — each with syntax, important options, and expected behaviour.

Mastery of these mechanisms turns the terminal from a place where you type individual commands into a programmable environment.

---

## Learning Objectives

By the end of this module you will be able to:

- Explain the difference between a shell built-in and an external command
- Predict how the shell performs expansion (globs, variables, command substitution, arithmetic)
- Redirect standard streams and construct pipelines
- Control jobs and background processes
- Inspect and modify the environment
- Use essential navigation, search, text-processing, process, network, and system tools with understanding of their purpose and common options
- Write small, safe command lines and simple scripts that behave predictably

---

## Prerequisites

- Modules 01–03 recommended (filesystem, users, permissions)
- Comfortable opening a terminal and running simple commands

---

## Core Concepts

### 1. What the Shell Does

When you type a line and press Enter the shell:

1. Reads the line.
2. Splits it into tokens (words and operators).
3. Performs expansions (see below).
4. Applies redirections.
5. Locates the command (built-in, function, or executable on `PATH`).
6. Executes it, possibly connecting pipes.
7. Waits (or not) for completion and reports the exit status.

Common interactive shells: **bash**, **zsh**, **fish**. Most scripts and examples in this curriculum assume a POSIX-oriented shell (bash or dash).

### 2. Built-ins vs External Commands

- **Built-in** — implemented inside the shell itself (`cd`, `export`, `read`, `ulimit`, …). No separate process is started.
- **External** — an executable file found via `$PATH` (`ls`, `grep`, `find`, `ps`, …).

```bash
type cd                 # builtin
type ls                 # external (hashed path)
type echo               # often a built-in
which ls                # full path of external command
command -v ls           # portable way to resolve a command
command -v cd           # shows "cd" is a shell builtin
```

**Why it matters:** Built-ins can change the shell’s own state (`cd` changes the current directory of the shell process). External commands run as child processes and cannot permanently change the parent shell’s working directory or variables unless you use constructs like `export` or command substitution deliberately.

### 3. Expansion (the Order Matters)

The shell performs several kinds of expansion before executing a command. A simplified practical order:

1. Brace expansion — `{a,b,c}`, `{1..5}`
2. Tilde expansion — `~`, `~alice`
3. Parameter / variable expansion — `$VAR`, `${VAR}`
4. Arithmetic expansion — `$(( ... ))`
5. Command substitution — `$( ... )` or `` `...` ``
6. Word splitting (on `$IFS`)
7. Pathname expansion (globs) — `*`, `?`, `[abc]`

```bash
echo {one,two,three}              # brace → one two three
echo ~/Documents                  # tilde → /home/you/Documents
NAME=alice; echo "Hello $NAME"    # parameter expansion
echo $(( 2 + 3 * 4 ))             # arithmetic → 14
echo "Today is $(date +%Y-%m-%d)" # command substitution
echo /usr/bin/py*                 # pathname expansion (globs)
```

Quotes change behaviour:

- Double quotes `"..."` — allow parameter, arithmetic, and command substitution; suppress word splitting and globbing.
- Single quotes `'...'` — no expansion at all.
- Unquoted — full expansion and word splitting.

```bash
VAR="a b c"
echo $VAR          # three words (word splitting)
echo "$VAR"        # one word
echo '$VAR'        # literal characters $ V A R
```

**Security note:** Unquoted variables that expand to empty or to values containing spaces/globs are a frequent source of bugs and, in scripts that call `rm` or similar, of dangerous behaviour. Prefer `"$VAR"` unless you intentionally want splitting.

### 4. Standard Streams and Redirection

Every process has three standard streams:

| File descriptor | Name | Default connection |
|-----------------|------|--------------------|
| 0 | stdin | keyboard |
| 1 | stdout | terminal |
| 2 | stderr | terminal |

Redirection operators:

```bash
command > file          # stdout to file (truncate existing content)
command >> file         # stdout append
command 2> file         # stderr to file
command &> file         # both stdout and stderr (bash)
command > file 2>&1     # stderr follows stdout (portable form)
command < file          # stdin from file
command << EOF          # here-document (stdin from following lines until EOF)
line1
line2
EOF
command <<< "text"      # here-string (bash) — stdin from a string
```

**Order matters for `2>&1`:**  
`command > file 2>&1` sends both streams to `file`.  
`command 2>&1 > file` first points stderr at the current stdout (usually the terminal), then redirects stdout to `file` — stderr still goes to the terminal.

### 5. Pipelines

A pipeline connects the stdout of one command to the stdin of the next:

```bash
command1 | command2 | command3
```

The exit status of a pipeline is normally the status of the **last** command. In bash, `set -o pipefail` makes the pipeline fail if **any** stage fails — recommended in scripts.

```bash
set -o pipefail
false | true
echo $?                 # 1 when pipefail is on; 0 when off
```

### 6. Exit Status

Every command returns a numeric exit status (0–255):

- `0` — success
- non-zero — failure (by convention)

```bash
ls /tmp
echo $?                 # 0 if /tmp exists and was listable

ls /nonexistent
echo $?                 # non-zero (often 2)

false
echo $?                 # 1
```

In scripts you test status with `if`, `&&`, `||`, and `set -e` (exit on first failure).

```bash
command1 && command2    # run command2 only if command1 succeeded
command1 || command2    # run command2 only if command1 failed
```

### 7. Job Control

```bash
long_command &          # start in background; shell prints job id and PID
jobs                    # list background/stopped jobs of this shell
jobs -l                 # include PIDs
fg %1                   # bring job 1 to foreground
bg %1                   # resume stopped job 1 in background
Ctrl-Z                  # suspend (stop) current foreground job
kill %1                 # send SIGTERM to job 1
kill -9 %1              # SIGKILL (last resort)
wait %1                 # wait for job 1 to finish
```

Job numbers (`%1`, `%2`, …) are per-shell. Process IDs (PIDs) are system-wide.

### 8. The Environment

A process inherits a set of name=value pairs called the environment.

```bash
printenv                # all environment variables
printenv PATH           # one variable
echo $PATH
echo $HOME
echo $USER
export MYVAR=value      # create/update and mark for export to children
env MYVAR=temp cmd      # run cmd with a one-off environment change
unset MYVAR             # remove from shell
```

Important variables:

| Variable | Typical purpose |
|----------|-----------------|
| `PATH` | Directories searched for executables (order matters) |
| `HOME` | User’s home directory |
| `USER` / `LOGNAME` | Username |
| `SHELL` | Login shell |
| `PWD` | Current working directory |
| `OLDPWD` | Previous working directory (used by `cd -`) |
| `IFS` | Internal field separator (word splitting) |
| `EDITOR` / `VISUAL` | Preferred text editor |
| `LANG` / `LC_*` | Locale and character encoding |

**PATH security:** Directories earlier in `PATH` are searched first. A writable directory early in `PATH` (or `.` in `PATH`) is a classic privilege-escalation and hijacking risk. Prefer absolute paths in critical scripts when predictability matters.

---

## Essential Commands — Detailed Reference

Each subsection lists the command, what it does, important options, and a short usage example with expected meaning.

### Navigation and Directory Inspection

#### `pwd` — print working directory

```bash
pwd                     # absolute path of current directory
pwd -P                  # resolve symlinks (physical path)
```

Shows where you are. Scripts often capture it: `BASE=$(pwd)`.

#### `cd` — change directory

```bash
cd /var/log             # absolute path
cd ../..                # relative: up two levels
cd                      # go to $HOME
cd -                    # go to previous directory ($OLDPWD)
cd ~alice               # alice’s home (if permitted)
```

Built-in; changes the shell’s own current directory. `cd` to a non-existent path fails and leaves you where you were.

#### `ls` — list directory contents

```bash
ls                      # names only
ls -l                   # long format: type, perms, links, owner, group, size, time, name
ls -la                  # include hidden (dot) files
ls -lhrt                # long, human sizes, reverse time (newest last) — useful for logs
ls -ld /etc             # list the directory itself, not its contents
ls -li                  # include inode numbers
ls -R                   # recursive (can be huge)
ls --color=auto         # colourise (often aliased)
```

**Long format columns (simplified):**  
type+perms | link count | owner | group | size | mtime | name

Do **not** parse `ls` output in scripts; use `find`, `stat`, or shell globs instead.

#### `file` — determine file type

```bash
file /etc/passwd        # "ASCII text"
file /bin/ls            # ELF executable, … 
file -b filename        # brief (no filename prefix)
file -i filename        # MIME type
```

Uses magic numbers and content heuristics, not just the extension. Useful when investigating unknown binaries or data files.

#### `stat` — detailed metadata

```bash
stat filename
stat -c '%n %a %U %G %s' filename   # custom format: name, mode, user, group, size
stat -c '%Y' filename               # mtime as epoch seconds
```

Shows inode, size, blocks, type, device, links, access/modify/change times, and permissions in multiple forms. Preferred over parsing `ls` when you need reliable fields.

#### `tree` — directory tree (if installed)

```bash
tree -L 2               # depth 2
tree -a -L 2            # include hidden
tree -d -L 3            # directories only
tree -h /var/log        # human sizes
```

Not always installed by default; install via package manager in the lab if needed.

#### `realpath` / `readlink` — resolve paths

```bash
realpath filename       # absolute path with symlinks resolved
readlink -f filename    # similar (GNU)
readlink symlink        # show immediate symlink target only
```

Essential when scripts must work with canonical paths.

---

### Finding Files and Commands

#### `find` — search the filesystem

```bash
find /path -name '*.log'                # name match (shell-style, quote the pattern)
find /path -iname '*.log'               # case-insensitive
find /path -type f                      # regular files only
find /path -type d                      # directories only
find /path -mtime -7                    # modified in last 7 days
find /path -mtime +30                   # modified more than 30 days ago
find /path -size +10M                   # larger than 10 MiB
find /path -user alice                  # owned by alice
find /path -perm -4000                  # setuid bit set
find /path -perm 644                    # exact mode
find /path -name '*.conf' -exec cp {} /backup/ \;
find /path -name '*.tmp' -delete        # careful: permanent delete
```

**Important:**

- `-name` patterns are matched against the basename; quote them so the shell does not expand them first.
- `-exec cmd {} \;` runs `cmd` once per file; `-exec cmd {} +` batches files (more efficient).
- Prefer `-print0` with `xargs -0` when names may contain spaces or newlines.

```bash
find /var/log -name '*.log' -print0 | xargs -0 grep -l 'error'
```

#### `locate` — fast name database search

```bash
locate passwd
locate -i '*.conf'                  # case-insensitive
locate -r '/etc/.*\.conf$'          # regex
```

Uses a prebuilt database (`updatedb`). Very fast, but may be stale and usually does not see files created after the last database update. Not a substitute for `find` when you need live results or permission-aware searches.

#### `which` / `type` / `command` — locate a command

```bash
which ls                    # path of external executable (may miss builtins/aliases)
type ls                     # reports alias, builtin, or file
type -a ls                  # all matches
command -v ls               # portable resolution
```

Prefer `type` or `command -v` in scripts when you need to know how the shell will resolve a name.

#### `whereis` — binary, source, man page locations

```bash
whereis ls
whereis -b python3          # binaries only
```

---

### Viewing and Text Processing

#### `cat` — concatenate and print

```bash
cat file
cat file1 file2             # concatenate
cat -n file                 # number all lines
cat -A file                 # show non-printing characters
```

Fine for short files. For large files prefer `less` or `tail`.

#### `less` / `more` — pagers

```bash
less file
less +F file                # follow mode (like tail -f); Ctrl-C then q to quit
less -N file                # line numbers
```

Inside `less`: `/pattern` search forward, `n` next match, `q` quit, `h` help.

#### `head` / `tail` — first / last lines

```bash
head file                   # first 10 lines
head -n 20 file
tail file                   # last 10 lines
tail -n 50 file
tail -f /var/log/syslog     # follow (live append)
tail -F /var/log/app.log    # follow and retry if file is rotated
tail -n +5 file             # from line 5 to end
```

`tail -f` / `journalctl -f` are standard for live log watching.

#### `wc` — count lines, words, bytes

```bash
wc file
wc -l file                  # lines only
wc -l file1 file2           # per-file and total
wc -c file                  # bytes
```

#### `grep` — print lines matching a pattern

```bash
grep pattern file
grep -n pattern file        # with line numbers
grep -i pattern file        # case-insensitive
grep -v pattern file        # invert (non-matching lines)
grep -E 'pat1|pat2' file    # extended regex
grep -R pattern dir         # recursive
grep -R --include='*.conf' pattern /etc
grep -l pattern files...    # only print filenames that match
grep -c pattern file        # count of matching lines
grep -A2 -B2 pattern file   # context: 2 lines after/before
```

Exit status: 0 if any match, 1 if no match, 2 on error. Useful in scripts:

```bash
if grep -q 'ERROR' /var/log/app.log; then
  echo "errors found"
fi
```

#### `cut` — remove sections of lines

```bash
cut -d: -f1 /etc/passwd                 # first field, colon delimiter
cut -d: -f1,7 /etc/passwd               # fields 1 and 7
cut -d: -f1-3 /etc/passwd               # fields 1 through 3
cut -c1-10 file                         # characters 1–10
```

Best for simple delimiter-separated data. For more complex field logic use `awk`.

#### `awk` — pattern scanning and processing

```bash
awk -F: '{print $1, $7}' /etc/passwd    # colon-separated; print fields 1 and 7
awk '/error/ {print $0}' file           # lines matching regex
awk '{sum += $1} END {print sum}' nums  # sum first column
awk -F, 'NR>1 {print $2}' data.csv      # skip header, print column 2
```

`NR` is the current record (line) number; `NF` is the number of fields; `$0` is the whole line; `$1`…`$n` are fields.

#### `sed` — stream editor

```bash
sed 's/old/new/' file                   # replace first occurrence per line
sed 's/old/new/g' file                  # replace all on each line
sed -n '10,20p' file                    # print lines 10–20
sed -i 's/old/new/g' file               # in-place edit (use with care; backup first)
sed '/^#/d' file                        # delete comment lines
```

`sed` is powerful; start with substitution and line selection before writing complex scripts.

#### `sort` / `uniq` — sort and report duplicates

```bash
sort file
sort -n file                            # numeric sort
sort -r file                            # reverse
sort -k2 file                           # sort by field 2
sort -t: -k3n /etc/passwd               # colon delimiter, numeric field 3
sort file | uniq                        # unique lines (input must be sorted)
sort file | uniq -c                     # count occurrences
sort file | uniq -c | sort -nr          # frequency ranking
```

Classic ranking pipeline:

```bash
cut -d: -f7 /etc/passwd | sort | uniq -c | sort -nr
```

#### `xargs` — build command lines from stdin

```bash
find . -name '*.tmp' -print0 | xargs -0 rm -f
echo 'a b c' | xargs -n 1 echo          # one arg per command
cat urls.txt | xargs -n1 curl -I        # carefully, in lab only
```

`-0` / `-print0` pair handles arbitrary filenames safely. Without `-0`, whitespace in names breaks arguments.

---

### Processes and Resources

#### `ps` — snapshot of processes

```bash
ps                      # processes in current terminal
ps aux                  # all processes, BSD-style columns
ps -ef                  # all processes, System V style
ps -u alice             # processes of user alice
ps -p 1234              # specific PID
ps -o pid,user,cmd -C sshd   # custom columns for processes named sshd
```

Common `ps aux` columns: USER, PID, %CPU, %MEM, VSZ, RSS, TTY, STAT, START, TIME, COMMAND.

STAT codes (selection): `R` running, `S` sleeping, `D` uninterruptible, `Z` zombie, `T` stopped, `+` foreground process group.

#### `top` / `htop` — interactive process viewer

```bash
top                     # press q to quit, h for help
htop                    # improved UI if installed
```

Useful for spotting CPU or memory hogs in real time. `htop` allows easier searching and tree view.

#### `pgrep` / `pkill` — find or signal by name

```bash
pgrep ssh               # PIDs matching name
pgrep -a ssh            # PIDs and full command line
pgrep -u alice          # processes of user
pkill -HUP nginx        # send SIGHUP to matching processes
pkill -u alice processname
```

Safer than parsing `ps` output for simple name-based selection.

#### `kill` / `killall` — send signals

```bash
kill 1234               # SIGTERM (default) — polite request to exit
kill -15 1234           # same
kill -HUP 1234          # SIGHUP — often “reload config”
kill -9 1234            # SIGKILL — force; process cannot catch it
kill -l                 # list signal names
killall processname     # by name (use carefully)
```

Prefer SIGTERM first; use SIGKILL only when the process does not respond.

#### `lsof` — list open files (if installed)

```bash
lsof -i                 # internet (network) sockets
lsof -i :22             # anything on port 22
lsof -u alice           # files opened by user
lsof /var/log/syslog    # who has this file open
lsof -p 1234            # files opened by PID
```

Extremely useful for “which process is using this port/file?” questions.

#### `ss` — socket statistics (modern replacement for much of netstat)

```bash
ss -tuln                # TCP/UDP listening sockets, numeric
ss -tulpn               # include process info (may need root)
ss -tan                 # all TCP, numeric
ss -tp                  # TCP with processes
ss -s                   # summary statistics
ss dst 192.0.2.10       # filter by destination
```

States include `LISTEN`, `ESTAB`, `TIME-WAIT`, etc. Prefer `ss` over `netstat` on modern Linux.

---

### Network (Basic Host Tools)

#### `ip` — show / manipulate interfaces, addresses, routes

```bash
ip link show            # interfaces and state
ip -br link             # brief
ip addr show            # addresses
ip -br addr
ip route show           # routing table
ip route get 8.8.8.8    # which path would be used
```

Replaces much of the older `ifconfig` / `route` tooling.

#### `ping` — ICMP echo

```bash
ping -c 4 host          # four probes then stop
ping -c 3 -W 2 host     # timeout per probe
```

Checks basic reachability and latency. Blocked by some firewalls.

#### `curl` — transfer data (HTTP and more)

```bash
curl -I https://example.com          # headers only (HEAD-like)
curl -v https://example.com          # verbose (request/response detail)
curl -o file https://example.com     # save body to file
curl -f -sS https://example.com      # fail on HTTP errors, silent but show errors
curl -X POST -H 'Content-Type: application/json' -d '{"a":1}' https://httpbin.org/post
```

Essential for API and web troubleshooting. Prefer `curl -v` when diagnosing TLS or redirect issues.

#### `dig` / `host` — DNS lookup

```bash
dig example.com
dig +short example.com
dig @8.8.8.8 example.com A
dig -x 8.8.8.8                       # reverse lookup
host example.com
```

`dig` is preferred for detailed DNS work; `+trace` walks the hierarchy from the root.

#### `nc` (netcat) — arbitrary TCP/UDP connections (lab use)

```bash
nc -zv host 22                       # scan/connect check (zero-I/O)
nc -l -p 12345                       # listen (lab only)
```

Powerful; restrict to authorized lab networks.

---

### System Information and Disk

#### `uname` — kernel and system identity

```bash
uname -a                # all
uname -r                # kernel release
uname -m                # machine architecture
```

#### `hostnamectl` — hostname and related data (systemd)

```bash
hostnamectl
hostnamectl status
```

#### `uptime` — how long the system has been running; load averages

```bash
uptime
```

Load averages are 1-, 5-, and 15-minute averages of runnable (and uninterruptible) processes.

#### `free` — memory usage

```bash
free -h                 # human-readable
free -m                 # mebibytes
```

Pay attention to **available** (or the calculation involving buff/cache) rather than only “free”.

#### `df` — disk space per filesystem

```bash
df -h                   # human sizes
df -hT                  # include filesystem type
df -i                   # inode usage (important when “no space” but df shows free)
```

#### `du` — disk usage of files/directories

```bash
du -sh *                # summary for each item in current directory
du -sh /var/log
du -h --max-depth=1 /var
du -xh /home            # stay on one filesystem
```

Combine with `sort` for ranking:

```bash
du -xh --max-depth=1 /var 2>/dev/null | sort -h
```

#### `mount` / `findmnt` — mounted filesystems

```bash
mount
findmnt
findmnt -D              # with sizes
findmnt /home
```

#### `journalctl` — systemd journal (logs)

```bash
journalctl -xe                  # recent, with explanations
journalctl -u sshd              # unit sshd
journalctl -f                   # follow
journalctl --since "1 hour ago"
journalctl -p err               # priority error and above
```

---

### Help and Documentation

#### `man` — manual pages

```bash
man ls
man 5 passwd            # section 5 (file formats)
man -k password         # search short descriptions (apropos)
```

Sections (common): 1 user commands, 2 system calls, 3 library, 5 file formats, 8 admin commands.

#### `--help` / `help`

```bash
ls --help
help cd                 # bash builtin help
help -d cd              # short description
```

---

## Detailed Explanation — A Complete Command Line

Consider:

```bash
find /var/log -name '*.log' -mtime -1 2>/dev/null | xargs grep -l 'error' | head
```

What happens step by step:

1. **`find /var/log -name '*.log' -mtime -1`**  
   Walks `/var/log`, selects regular pathnames whose **basename** matches `*.log` and whose modification time is within the last 24 hours. The pattern is quoted so the shell does not expand it before `find` sees it.

2. **`2>/dev/null`**  
   Discards error messages (e.g. permission denied on some subdirectories). Useful for cleaner output; in investigations you may want to keep or log those errors instead.

3. **`| xargs grep -l 'error'`**  
   Takes the list of paths on stdin and runs `grep -l 'error'` on them (possibly in batches). `-l` prints only the names of files that contain at least one match, not the matching lines.

4. **`| head`**  
   Limits output to the first 10 lines (default) so a large result set does not flood the terminal.

Understanding each piece lets you modify the pipeline safely — for example, adding `-print0` / `xargs -0` for unusual filenames, or replacing `head` with `wc -l` to count matching files.

---

## Practical Examples

### Safe temporary files and cleanup

```bash
TMP=$(mktemp)
echo "work data" > "$TMP"
# ... use "$TMP" ...
rm -f -- "$TMP"
```

`mktemp` creates a unique file with safe permissions. Always quote and prefer `--` before variable paths when calling `rm`.

### Ranking login shells

```bash
cut -d: -f7 /etc/passwd | sort | uniq -c | sort -nr
```

### Live log follow

```bash
tail -F /var/log/syslog
# or on systemd systems:
journalctl -f -u sshd
```

### Process inspection without fragile greps

```bash
pgrep -a ssh
ps -o pid,user,cmd -C sshd
```

### What is listening

```bash
ss -tulpn
sudo ss -tulpn | grep ':22'
```

### Largest items under /var

```bash
sudo du -xh --max-depth=1 /var 2>/dev/null | sort -hr | head
```

---

## Common Mistakes

| Mistake | Consequence | Better approach |
|---------|-------------|-----------------|
| Unquoted variables that contain spaces | Word splitting breaks the command | Always quote: `"$VAR"` |
| `rm -rf $DIR` when `DIR` is empty or wrong | Can expand dangerously | Quote; use `rm -rf -- "$DIR"`; test with `echo` first |
| Ignoring exit status in scripts | Silent failures | `set -euo pipefail` near the top of scripts |
| Parsing `ls` output | Fragile with special characters | Use `find`, `stat`, globs, or proper libraries |
| Running entire pipelines as root | Unnecessary privilege | Elevate only the commands that need it |
| Forgetting that `>` truncates | Accidental data loss | Use `>>` to append, or confirm the target |
| `find … -name *.log` without quotes | Shell expands the glob too early | Always quote patterns: `-name '*.log'` |
| Using `kill -9` first | No chance for clean shutdown | Try SIGTERM (default) first |

---

## Best Practices

- Quote variables and command substitutions unless you deliberately want word splitting.
- Prefer long options in scripts (`--recursive` instead of `-R`) for readability when available.
- Use `set -euo pipefail` in bash scripts as a sensible default, then relax selectively.
- Keep interactive exploration and production scripts distinct; test scripts on non-critical data.
- Learn `man` and `--help`; they are faster than searching the web for basic flag questions.
- Build pipelines incrementally: run the first stage, then add the next, checking output each time.
- Prefer `ss` over `netstat`, `ip` over `ifconfig`, and `pgrep` over `ps | grep` for clarity and robustness.
- Treat filenames as arbitrary bytes: use `-print0` / `xargs -0` or `find -exec` when passing many paths.

---

## Hands-on Exercise

1. Demonstrate the difference between unquoted, double-quoted, and single-quoted variables that contain spaces.
2. Write a pipeline that lists the five largest directories under `/var` (hint: `du` + `sort` + `head`).
3. Use `find` to locate files under your home directory modified in the last 24 hours; then limit the listing with `head`.
4. Start a long-running command in the background (`sleep 300 &`), list jobs, bring it to the foreground, suspend it with Ctrl-Z, resume it in the background, then kill it.
5. Inspect your `PATH` and explain why the order of directories matters for security and predictability.
6. Use `ss -tulpn` and identify at least two listening services and their PIDs (if visible).
7. Build a pipeline with `cut`, `sort`, `uniq -c`, and `sort -nr` on `/etc/passwd` to rank shells or UIDs.

---

## Review Questions

1. What is the difference between a shell built-in and an external command? How can you tell which one `cd` is?
2. Why does `echo $VAR` sometimes produce multiple words while `echo "$VAR"` produces one?
3. What do the numbers 0, 1, and 2 represent in the context of redirection?
4. How do you redirect both stdout and stderr to the same file?
5. What exit status conventionally indicates success?
6. What does `Ctrl-Z` do to a foreground process?
7. Why is parsing the output of `ls` considered a bad practice?
8. What is the difference between a capture of `find … -name *.log` and `find … -name '*.log'`?
9. When would you choose `pgrep -a name` over `ps aux | grep name`?
10. Why might `df -h` show free space while creating a file still fails with “No space left on device”?

---

## Summary

- The shell is a programming environment that performs expansion, redirection, and job control before executing commands.
- Understanding expansion and quoting prevents an entire class of bugs and security issues.
- Pipelines and redirection let you compose small tools into powerful one-liners and scripts.
- Exit status, job control, and the environment are essential for reliable automation.
- A solid command vocabulary — `find`, `grep`, `awk`, `sed`, `ps`/`pgrep`, `ss`, `ip`, `du`/`df`, `journalctl`, and friends — covers the majority of daily investigation and administration work on Linux.
- Prefer safe patterns: quote variables, use null-delimited pipelines for filenames, elevate privileges only where required, and build complex commands step by step.

---

## Sources

- man pages: `bash(1)`, `find(1)`, `grep(1)`, `awk(1)`, `sed(1)`, `ps(1)`, `ss(8)`, `ip(8)`, `journalctl(1)`, `xargs(1)`
- POSIX shell specification (for portable behaviour)
- Distribution documentation on coreutils and util-linux
