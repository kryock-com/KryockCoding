package com.example.intentexample;

import androidx.appcompat.app.AppCompatActivity;


import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class SecondActivity extends AppCompatActivity {
    private Button second;
    private TextView secondLBL;
    private EditText secondInfo;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.second_activity);
        second = findViewById(R.id.secondBTN);
        secondLBL = findViewById(R.id.secondLBL);
        secondInfo = findViewById(R.id.SecondUI);

        String valueOfIntent = getIntent().getStringExtra("User Input");
        secondLBL.setText(valueOfIntent);


        second.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String seLBL = String.valueOf(secondLBL.getText());
                String infoLBL = String.valueOf(secondInfo.getText());
                String ui = (seLBL+infoLBL);

                Intent i = new Intent(SecondActivity.this,OtherActivity.class);
                i.putExtra("User Input", ui);


                startActivity(i);
            }
        });

    }

}

