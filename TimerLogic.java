import javax.swing.*;
import java.awt.Color;

public class TimerLogic {
    private JLabel timerLabel;
    private JLabel tipOffLabel;
    private Timer timer;
    private Timer tipOffTimer;
    private int remainingTime; // Zeit in Zehntelsekunden
    private int tipOffRemainingTime; // Zeit in Sekunden für den Tip-Off-Countdown
    private boolean isPaused;
    private float fontSize = 100.0f; // Startgröße der Schrift

    public TimerLogic(JLabel timerLabel, JLabel tipOffLabel, int initialTime, int tipOffTime) {
        this.timerLabel = timerLabel;
        this.tipOffLabel = tipOffLabel;
        this.remainingTime = initialTime;
        this.tipOffRemainingTime = tipOffTime;
        this.isPaused = false;
            timer = new Timer(1000, e -> {
                if (remainingTime > 0) {
                    remainingTime--;
                    // Aktualisieren Sie hier das Timer-Label
                } else {
                    ((Timer)e.getSource()).stop();
                }
            });
    }
  //      timer.start();        // Starte den Timer
  //      tipOffTimer.start();  // Starte den Tip-Off-Timer  
        //updateTimerLabel();  // Aktualisiere das Timer-Label 
        //updateTipOffLabel(); // Aktualisiere das Tip-Off-Label

    public void startMainTimer(int timeInSeconds) {
        remainingTime = timeInSeconds;
        timer.start();
    }

    public void startTipOffTimer() {
        if (!tipOffTimer.isRunning()) {
            tipOffTimer.start();
        }
    }

    public void pauseOrResumeTimer() {
        isPaused = !isPaused;
        if (isPaused) {
            timer.stop();
            tipOffTimer.stop();
        } else {
            timer.start();
            tipOffTimer.start();
        }
    }

    public void adjustTime(int tenthsOfSeconds) {
        remainingTime += tenthsOfSeconds;
        updateTimerLabel();
    }

    public void toggleScreenBlack() {
        if (timerLabel.getForeground().equals(Color.BLACK)) {
            timerLabel.setForeground(Color.RED); // Ändere Textfarbe zu Rot
        } else {
            timerLabel.setForeground(Color.BLACK); // Ändere Textfarbe zu Schwarz
        }
    }

    public void changeFontSize(float sizeChange) {
        fontSize += sizeChange;
        if (fontSize < 10.0f) {
            fontSize = 10.0f; // Setze ein Minimum für die Schriftgröße
        }
        timerLabel.setFont(timerLabel.getFont().deriveFont(fontSize));
    }

    private void updateTimerLabel() {
        int seconds = remainingTime / 10;
        int tenthsOfSecond = remainingTime % 10;
        timerLabel.setText(String.format("%02d:%d", seconds, tenthsOfSecond));
    }

    private void updateTipOffLabel() {
        int minutes = tipOffRemainingTime / 60;
        int seconds = tipOffRemainingTime % 60;
        tipOffLabel.setText(String.format("%02d:%02d", minutes, seconds));
    }

    // Weitere Methoden, wie Anpassung der Zeit oder zusätzliche Funktionen, können hier hinzugefügt werden
}
