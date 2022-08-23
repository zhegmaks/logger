import java.io.IOException;
import java.util.logging.FileHandler;
import java.util.logging.Handler;
import java.util.logging.SimpleFormatter;
import  java.util.logging.*;

public class Logger {

    Logger LOGGER = java.util.logging.Logger.getLogger(getClass().getName());

    private static Logger instance;

    public Logger() {

    }

    public static synchronized Logger getInstance() { // singleton
        if (instance == null) {
            instance = new Logger();
        }
        return instance;
    }

    public void sendLog(String message) {
        try {
            Handler fileHandler = null;
            fileHandler = new FileHandler("logs/logfile.log", true); // create log file
            SimpleFormatter simple = new SimpleFormatter();
            fileHandler.setFormatter(simple);
            LOGGER.addHandler(fileHandler); // add file handler
            LOGGER.info(message);
            fileHandler.close();
        } catch(IOException exception) {
            System.out.println(exception);
        }
    }
}