import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent; // Add this import statement
import java.awt.event.KeyEvent;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyListener;
import java.awt.event.ActionListener; // Add this import statement
import javax.swing.AbstractAction; // Add this import statement


public class TimerScreen {
    private JFrame frame;
    private JLabel timerLabel;
    private JLabel tipOffLabel;
    private TimerLogic timerLogic;

    public TimerScreen(int initialTime, int tipOffTime) {
        frame = new JFrame("Timer App");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        addKeyBindings();
    }

    private void addKeyBindings() {
        frame.getRootPane().getInputMap(JComponent.WHEN_IN_FOCUSED_WINDOW).put(KeyStroke.getKeyStroke("SPACE"), "pauseResume");
        frame.getRootPane().getActionMap().put("pauseResume", new AbstractAction() {
            @Override
            public void actionPerformed(ActionEvent e) {
                timerLogic.pauseOrResumeTimer();
            }
        });
        frame.addKeyListener(new KeyAdapter() {
            @Override
            public void keyPressed(KeyEvent e) {
                switch (e.getKeyCode()) {
                    case KeyEvent.VK_1:
                        timerLogic.startMainTimer(240); // Startet den Haupttimer mit 24 Sekunden
                        break;
                    case KeyEvent.VK_2:
                        timerLogic.startMainTimer(140); // Startet den Haupttimer mit 14 Sekunden
                        break;
                    case KeyEvent.VK_3:
                        timerLogic.adjustTime(10); // Erhöht die Zeit um eine Sekunde
                        break;
                    case KeyEvent.VK_4:
                        timerLogic.adjustTime(-10); // Verringert die Zeit um eine Sekunde
                        break;
                    case KeyEvent.VK_5:
                        timerLogic.toggleScreenBlack(); // Wechselt die Bildschirmfarbe
                        break;
                    case KeyEvent.VK_6:
                        timerLogic.changeFontSize(10.0f); // Erhöht die Schriftgröße
                        break;
                    case KeyEvent.VK_7:
                        timerLogic.changeFontSize(-10.0f); // Verringert die Schriftgröße
                        break;
                    case KeyEvent.VK_SPACE:
                        timerLogic.pauseOrResumeTimer(); // Pausiert oder setzt den Timer fort
                        break;
                }
            }
        });
    }
    public void show() {
    }
}
// Compare this snippet from TimerScreen.java:
// import javax.swing.*;
// import java.awt.*;

// public class TimerScreen {
//     private JFrame frame;
