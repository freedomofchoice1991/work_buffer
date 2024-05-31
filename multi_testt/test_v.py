import signal
import logging
import sys
from sqlalchemy.orm.session import close_all_sessions
import os


class SystemCallsManager:
    def __init__(self, pid):
        self.pid = pid

        # Registration for each signal
        signal_and_signal_handlers = [
            (signal.SIGHUP, self.sighup_handler),
            (signal.SIGINT, self.sigint_handler),
            (signal.SIGQUIT, self.sigquit_handler),
            (signal.SIGILL, self.sigill_handler),
            (signal.SIGTRAP, self.sigtrap_handler),
            (signal.SIGABRT, self.sigabrt_handler),
            (signal.SIGBUS, self.sigbus_handler),
            (signal.SIGFPE, self.sigfpe_handler),
            (signal.SIGUSR1, self.sigusr1_handler),
            (signal.SIGSEGV, self.sigsegv_handler),
            (signal.SIGUSR2, self.sigusr2_handler),
            (signal.SIGPIPE, self.sigpipe_handler),
            (signal.SIGALRM, self.sigalrm_handler),
            (signal.SIGTERM, self.sigterm_handler),
            (signal.SIGCHLD, self.sigchld_handler),
            (signal.SIGCONT, self.sigcont_handler),
            (signal.SIGTSTP, self.sigtstp_handler),
            (signal.SIGTTIN, self.sigttin_handler),
            (signal.SIGTTOU, self.sigttou_handler),
            (signal.SIGURG, self.sigurg_handler),
            (signal.SIGXCPU, self.sigxcpu_handler),
            (signal.SIGXFSZ, self.sigxfsz_handler),
            (signal.SIGVTALRM, self.sigvtalrm_handler),
            (signal.SIGPROF, self.sigprof_handler),
            (signal.SIGWINCH, self.sigwinch_handler),
            (signal.SIGIO, self.sigio_handler),
            (signal.SIGPWR, self.sigpwr_handler),
            (signal.SIGSYS, self.sigsys_handler)
        ]

        for sig, handler in signal_and_signal_handlers:
            try:
                signal.signal(sig, handler)
            except OSError as err:
                logging.info(f'Failed to set signal handler for {sig}: {err}')

    def cleanup(self):
        print('Performing cleanup before exiting...')
        # newer version of session.close_all()
        close_all_sessions()
        os._exit(1)

    def sighup_handler(self, signum, frame):
        logging.info(f"Process {self.pid} has "
                     f"received {signal.Signals(signum).name} signal, perhaps terminal session was closed.")
        logging.info("This signal is ignored since the process is working as daemon. "
                     "You may want to add a config reloader for the daemon process.\n")
        # No action needed because the process is on going and terminal was closed.

    def sigint_handler(self, signum, frame):
        logging.info(f"Process {self.pid} has received {signal.Signals(signum).name} signal.\n")
        # Finalize and save everything and exit gracefully
        self.cleanup()

    def sigquit_handler(self, signum, frame):
        logging.info(f"Process {self.pid} has received {signal.Signals(signum).name} signal by ctrl + \\.\n")
        # Finalize and save everything and exit gracefully
        self.cleanup()

    def sigill_handler(self, signum, frame):
        logging.info(f"Process {self.pid} has received {signal.Signals(signum).name} signal")
        logging.info('***THIS IS A SERIOUS PROBLEM***')
        logging.info('CPU encountered illegal instruction. Check the integrity of code and '
                     'make sure your code and data have not been corrupted\n')
        # Finalize and save everything and exit gracefully
        self.cleanup()

    def sigtrap_handler(self, signum, frame):
        logging.info(f"Process {self.pid} has received {signal.Signals(signum).name} signal")
        logging.info('This was a trap for debugging purpose by programmer. Ensure no debugger is unintentionally'
                     ' attached to your process. Examine the code around the breakpoint or'
                     ' trap instruction to understand why it was triggered.\n')
        # Finalize and save everything and exit gracefully
        self.cleanup()

    def sigabrt_handler(self, signum, frame):
        logging.info(f"Process {self.pid} has received {signal.Signals(signum).name} signal")
        logging.info('This is a call to Abort the mission. Program can not continue safely. Code needs to be debugged.\n')
        # Finalize and save everything and exit gracefully
        self.cleanup()

    def sigbus_handler(self, signum, frame):
        logging.info(f"Process {self.pid} has received {signal.Signals(signum).name} signal")
        logging.info('This critical error indicates either "Unaligned Memory Access", "Invalid Physical Address",'
                     ' "Hardware Errors" or "Memory-mapped Files"\n')
        # Finalize and save everything and exit gracefully
        self.cleanup()

    def sigfpe_handler(self, signum, frame):
        logging.info(f"Process {self.pid} has received {signal.Signals(signum).name} signal")
        logging.info('Check for Underflow, Overflow, Division by Zero or Invalid operation in the code.\n')
        # Finalize and save everything and exit gracefully
        self.cleanup()

    def sigusr1_handler(self, signum, frame):
        logging.info(f"Process {self.pid} has received {signal.Signals(signum).name} signal")
        logging.info('This is a user defined signal and for this program due to our intention will be ignored.\n')

    def sigsegv_handler(self, signum, frame):
        logging.info(f"Process {self.pid} has received {signal.Signals(signum).name} signal")
        logging.info("Critical problem. Program violated memory access default. It should be taken care of.\n")
        self.cleanup()

    def sigusr2_handler(self, signum, frame):
        logging.info(f"Process {self.pid} has received {signal.Signals(signum).name} signal")
        logging.info('This is a user defined signal and for this program due to our intention will be ignored.\n')

    def sigpipe_handler(self, signum, frame):
        logging.info(f"Process {self.pid} has received {signal.Signals(signum).name} signal")
        logging.info("Happened due to broken pipe.\n")
        # Finalize and save everything and exit gracefully
        self.cleanup()

    def sigalrm_handler(self, signum, frame):
        logging.info(f"Process {self.pid} has received {signal.Signals(signum).name} signal")
        logging.info('For this program Alarm will be ignored because we have not set any so far.\n')

    def sigterm_handler(self, signum, frame):
        logging.info(f"Process {self.pid} has received {signal.Signals(signum).name} signal")
        logging.info("Termination signal will end this process after the proper cleanup.\n")
        # Finalize and save everything and exit gracefully
        self.cleanup()

    def sigchld_handler(self, signum, frame):
        logging.info(f"Process {self.pid} has received {signal.Signals(signum).name} signal")
        logging.info("Signal indicates that a child process to this process was terminated.\n")

    def sigcont_handler(self, signum, frame):
        logging.info(f"Process {self.pid} has received {signal.Signals(signum).name} signal")
        logging.info("Resuming execution of a suspended process\n")
        # logic to resume the suspended process

    def sigtstp_handler(self, signum, frame):
        logging.info(f"Process {self.pid} has received {signal.Signals(signum).name} signal by ctrl + z")
        logging.info("Process is suspended right now. by pushing fg bring it to foreground again.\n")

    def sigttin_handler(self, signum, frame):
        logging.info(f"Process {self.pid} has received {signal.Signals(signum).name} signal")
        logging.info("This signal is intended to notify the process about terminal input restrictions "
                     "without allowing it to intercept or handle the signal.\n")

    def sigttou_handler(self, signum, frame):
        logging.info(f"Process {self.pid} has received {signal.Signals(signum).name} signal")
        logging.info("This signal is intended to notify the process about terminal output restrictions "
                     "without allowing it to intercept or handle the signal.\n")

    def sigurg_handler(self, signum, frame):
        logging.info(f"Process {self.pid} has received {signal.Signals(signum).name} signal")
        logging.info("This is a notification where process needs to handle out-of-band data on a socket.\n")

    def sigxcpu_handler(self, signum, frame):
        logging.info(f"Process {self.pid} has received {signal.Signals(signum).name} signal")
        logging.info("This process has exceeded process time limit and will be shutdown gracefully after cleanup.\n")
        # Finalize and save everything and exit gracefully
        self.cleanup()

    def sigxfsz_handler(self, signum, frame):
        logging.info(f"Process {self.pid} has received {signal.Signals(signum).name} signal")
        logging.info("Exceeded maximum of file size and needs to close files and cleanup resources.\n")
        # Finalize and save everything
        self.cleanup()

    def sigvtalrm_handler(self, signum, frame):
        logging.info(f"Process {self.pid} has received {signal.Signals(signum).name} signal")
        logging.info("For this program we just ignore it because we are not working with virtual timers.\n")

    def sigprof_handler(self, signum, frame):
        logging.info(f"Process {self.pid} has received {signal.Signals(signum).name} signal")
        logging.info('The profiling timer has expired. However for our program we just ignore it.\n')

    def sigwinch_handler(self, signum, frame):
        logging.info(f"Process {self.pid} has received {signal.Signals(signum).name} signal")
        logging.info('The window size of the terminal has changed.\n')

    def sigio_handler(self, signum, frame):
        logging.info(f"Process {self.pid} has received {signal.Signals(signum).name} signal")
        logging.info("I/O is possible on a file descriptor.\n")

    def sigpwr_handler(self, signum, frame):
        logging.info(f"Process {self.pid} has received {signal.Signals(signum).name} signal")
        logging.info('A power failure has been detected. Cleanup as soon as possible and then shutdown gracefully.\n')
        # Finalize and save everything and exit gracefully
        self.cleanup()

    def sigsys_handler(self, signum, frame):
        logging.info(f"Process {self.pid} has received {signal.Signals(signum).name} signal")
        logging.info("This process tried to make an unauthorized system call. Check the program for a exploit.\n")
        # Finalize and save everything and exit gracefully
        self.cleanup()

