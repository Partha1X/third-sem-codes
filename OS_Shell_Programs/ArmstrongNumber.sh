: << COMMENT
command-line shell or Shell : 
A shell is a command-line interface that acts as an intermediary between the user and the operating system (OS).
It provides a way for users to interact with the computer by typing commands and receiving responses.
Shells play a crucial role in facilitating communication and control over the operating system.
Here are some reasons why shells are essential for operating systems:
1.User Interface:CLI
2.Automation and Scripting:
3.System Control:
4.Resource Management:
5.Programming and Scripting:
6.Remote Access:
7.Customization
8.Batch Processing:
9.Debugging and Troubleshooting:
10.Multi-User Environments:

~:The term "shell" in the context of computing refers to a command-line interpreter that acts as a user interface to interact with the operating system. 
he name "shell" was chosen because it serves as an outer layer or interface between the user and the kernel (core) of the operating system.

Here's a metaphorical explanation:
1. Kernel: The kernel is the core part of the operating system that directly interacts with hardware and manages system resources.
2. Shell: The shell is like the outer layer or protective covering. It provides a way for users to communicate with the kernel. 
Users interact with the shell by entering commands, and the shell interprets these commands and communicates with the kernel to execute them.

In essence, the shell is a user-friendly interface that shields users from the complexities of interacting directly with the kernel.
It interprets user commands, executes them, and returns the results, creating a bridge between the user and the underlying system.

The name "shell" was likely chosen because it reflects this idea of an "outer layer or covering that encapsulates the inner workings" of the operating system.
Different shells, such as Bash, PowerShell, or the C Shell, have evolved over time with varying features and syntax,
but they all share the common purpose of providing a command-line interface to interact with the operating system.

[ Code is written in Bash, which is a popular Unix shell.
Bash (Bourne Again SHell) is a scripting language widely
used on Unix-like operating systems for automating tasks,
writing scripts, and running commands in a shell environment.
It is an enhanced version of the original Bourne Shell (sh) with additional features.
{various types of shell languages or shells- sh (Bourne Shell),Bash (Bourne Again SHell),csh (C Shell)
tcsh (Tenex C Shell),ksh (Korn Shell),zsh (Z Shell),fish (Friendly Interactive SHell)}
{On Windows, the default command-line shell is called Command Prompt, and it uses the command processor "cmd.exe".
However, in more recent versions of Windows, PowerShell has become increasingly popular and is often the default shell.
~Batch scripting is a type of scripting language used in the context of the Windows Command Prompt (cmd.exe). Batch scripts,
also known as batch files or shell scripts, are plain text files containing a series
of commands and instructions that the Command Prompt can execute sequentially.(".bat" extension.)


Windows Subsystem for Linux (WSL):
~For Windows 10 and later versions, Microsoft introduced WSL,
which allows running a Linux distribution alongside the Windows operating system.
~WSL provides a Linux-like environment, including a choice of various Linux shells such as Bash. ]
COMMENT
# WAP to Check Whether a Given Number is Armstrong or Not


echo -n "Enter a Number: "
read n
s=0
temp=$n

while ((n!=0)); do
    r=$((n%10))
    s=$((s+r*r*r))
    n=$((n/10))
done

if ((s==temp)); then
    echo "The Number $temp is Armstrong"
else
    echo "The Number $temp is Not Armstrong"
fi
