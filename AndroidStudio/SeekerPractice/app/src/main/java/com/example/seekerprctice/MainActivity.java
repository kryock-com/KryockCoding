package com.example.seekerprctice;

import androidx.appcompat.app.AppCompatActivity;
import androidx.constraintlayout.widget.ConstraintLayout;

import android.graphics.Color;
import android.os.Bundle;
import android.widget.SeekBar;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {
    private TextView message;
    private SeekBar seeker;

    private SeekBar Rseeker;
    private SeekBar Bseeker;
    private SeekBar Gseeker;

    private TextView value;
    private ConstraintLayout screen;

    String Rhex ="";
    String Bhex ="";
    String Ghex ="";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        //link the java to the widget
        message = findViewById(R.id.messageTXT);
        seeker = findViewById(R.id.seekBar);

        Rseeker = findViewById(R.id.RseekBar);
        Bseeker = findViewById(R.id.BseekBar);
        Gseeker = findViewById(R.id.GseekBar);

        value = findViewById(R.id.progressTXT);
        screen = findViewById(R.id.constraintLayout);



        //          progess / 150
        value.setText(seeker.getProgress() + "/" + seeker.getMax());

        //getting the progress of the seeker
        seeker.setOnSeekBarChangeListener(new SeekBar.OnSeekBarChangeListener() {
            //whenever you are sliding it
            int pval = 0;


            @Override
            public void onProgressChanged(SeekBar seekBar, int progress, boolean b) {
                //whenever you are sliding it
                message.setTextSize(progress+1);
                pval = progress;
                value.setText(pval + "/" + seeker.getMax());
            }

            @Override
            public void onStartTrackingTouch(SeekBar seekBar) {
                //whenever you click on it
            }

            @Override
            public void onStopTrackingTouch(SeekBar seekBar) {
                //whenever you release the seekbar

            }
        });

        Rseeker.setOnSeekBarChangeListener(new SeekBar.OnSeekBarChangeListener() {
            @Override
            public void onProgressChanged(SeekBar seekBar, int i, boolean b) {
                updateBackground();
            }

            @Override
            public void onStartTrackingTouch(SeekBar seekBar) {

            }

            @Override
            public void onStopTrackingTouch(SeekBar seekBar) {

            }
        });

        Bseeker.setOnSeekBarChangeListener(new SeekBar.OnSeekBarChangeListener() {
            @Override
            public void onProgressChanged(SeekBar seekBar, int i, boolean b) {
                updateBackground();
            }

            @Override
            public void onStartTrackingTouch(SeekBar seekBar) {

            }

            @Override
            public void onStopTrackingTouch(SeekBar seekBar) {

            }
        });

        Gseeker.setOnSeekBarChangeListener(new SeekBar.OnSeekBarChangeListener() {
            @Override
            public void onProgressChanged(SeekBar seekBar, int i, boolean b) {
                updateBackground();
            }

            @Override
            public void onStartTrackingTouch(SeekBar seekBar) {

            }

            @Override
            public void onStopTrackingTouch(SeekBar seekBar) {

            }
        });



    }
    private void updateBackground(){
        int r = Rseeker.getProgress();
        int b= Bseeker.getProgress();
        int g = Gseeker.getProgress();
        int colorVal = 0xff000000
                + r * 0x10000
                + g * 0x100
                + b;
        screen.setBackgroundColor(colorVal);

    }
}