package com.example.simplecalc;     //unique id for your program

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.text.Editable;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import java.text.BreakIterator;

public class MainActivity extends AppCompatActivity {

    private EditText number1TXT;
    private EditText number2TXT;
    private Button addBTN;
    private Button divBTN;
    private Button mulBTN;
    private TextView output;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);     //this line links the two files

        number1TXT = findViewById(R.id.number1);
        number2TXT = findViewById(R.id.number2);
        addBTN = findViewById(R.id.addBTN);
        divBTN = findViewById(R.id.divBTN);
        mulBTN = findViewById(R.id.muiltBTN);
        output = findViewById(R.id.output);

        divBTN.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Integer num1 = Integer.valueOf(String.valueOf(number1TXT.getText()));
                Integer num2 = Integer.valueOf(String.valueOf(number2TXT.getText()));
                int answer = num1 / num2;
                output.setText(String.valueOf(answer));
            }
        });

        mulBTN.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Integer num1 = Integer.valueOf(String.valueOf(number1TXT.getText()));
                Integer num2 = Integer.valueOf(String.valueOf(number2TXT.getText()));
                int answer = num1 * num2;
                output.setText(String.valueOf(answer));
            }
        });



    }



    //adding and subtracting are for hard coding the onclick
    public void adding(View v) {
        Integer num1 = Integer.valueOf(String.valueOf(number1TXT.getText()));
        Integer num2 = Integer.valueOf(String.valueOf(number2TXT.getText()));
        int answer = num1 + num2;
        output.setText(String.valueOf(answer));
    }
    public void subtract(View v) {
        Integer num1 = Integer.valueOf(String.valueOf(number1TXT.getText()));
        Integer num2 = Integer.valueOf(String.valueOf(number2TXT.getText()));
        int answer = num1 - num2;
        output.setText(String.valueOf(answer));
    }



}