package com.example.intentexample;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class MainActivity extends AppCompatActivity {
    private Button first;
    private EditText firstInfo;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        first = findViewById(R.id.FirstBTN);
        firstInfo = findViewById(R.id.FirstUI);
        first.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String ui = String.valueOf(firstInfo.getText());
                Intent  i = new Intent(MainActivity.this,SecondActivity.class);
                i.putExtra("User Input", ui);


                startActivity(i);
            }
        });

    }
}