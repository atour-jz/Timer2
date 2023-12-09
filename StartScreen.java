import javax.swing.*;
import java.awt.*;

public class StartScreen {
    private JFrame frame;

    public StartScreen() {
        frame = new JFrame("Shot Clock Auswahl");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new FlowLayout());

        JButton shotClock24Button = new JButton("24 Sekunden Shot Clock");
        shotClock24Button.addActionListener(e -> {
            openTimerScreen(240, 180); // 24 Sekunden und 3 Minuten für Tip-Off
        });

        JButton shotClock14Button = new JButton("14 Sekunden Shot Clock");
        shotClock14Button.addActionListener(e -> {
            openTimerScreen(140, 180); // 14 Sekunden und 3 Minuten für Tip-Off
        });

        frame.add(shotClock24Button);
        frame.add(shotClock14Button);
    }

    public void show() {
        frame.pack();
        frame.setVisible(true);
    }

    private void openTimerScreen(int initialTime, int tipOffTime) {
        TimerScreen timerScreen = new TimerScreen(initialTime, tipOffTime);
        timerScreen.show();
        frame.dispose();
    }
}
