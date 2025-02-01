package com.example.chirstmascountdown;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.os.Handler;
import android.provider.ContactsContract;
import android.widget.TextView;

import java.io.IOException;
import java.nio.CharBuffer;
import java.text.SimpleDateFormat;
import java.util.Date;

public class MainActivity extends AppCompatActivity {
    private TextView txtTimerDay,txtTimerHour,txtTimerMinute,txtTimerSecond;
    private Handler handler;
    private Runnable runnable;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        txtTimerDay = findViewById(R.id.txtTimerDay);
        txtTimerHour = findViewById(R.id.txtTimerHour);
        txtTimerMinute = findViewById(R.id.txtTimerMinute);
        txtTimerSecond = findViewById(R.id.txtTimerSecond);

        countDownStart();

    }

    public void countDownStart() {
        handler = new Handler();
        runnable = new Runnable() {
            @Override
            public void run() {
                handler.postDelayed(this,1000); //pause this activity for 1000 millisec
                try {
                    SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd");
                    Date futureDate = dateFormat.parse("2022-12-25");
                    Date currentDate = new Date();

                    long diff = futureDate.getTime() - currentDate.getTime();
                    long day = diff/(24*60*60*1000);
                    diff -= day * (24*60*60*1000);
                    txtTimerDay.setText(""+String.format("%02d",day));

                    long hour = diff/(60*60*1000);
                    diff -= hour * (60*60*1000);
                    txtTimerHour.setText(""+String.format("%02d",hour));

                    long minutes = diff/(60*1000);
                    diff -= minutes * (60*1000);
                    txtTimerMinute.setText(""+String.format("%02d",minutes));

                    long second = diff/(1000);
                    diff -= second * (1000);
                    txtTimerSecond.setText(""+String.format("%02d",second));
                }
                catch(Exception e){
                    e.printStackTrace();
                }
            }
        };
        handler.postDelayed(runnable,1000);
    }
}