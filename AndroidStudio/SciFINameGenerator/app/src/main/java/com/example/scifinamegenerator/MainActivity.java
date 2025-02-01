package com.example.scifinamegenerator;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {
    //defineing the widget variable
    EditText firstNameTXT;
    EditText lastNameTXT;
    EditText cityNameTXT;
    EditText schoolNameTXT;
    EditText brotherNameTXT;
    EditText sisterNameTXT;
    Button generateBTN;
    TextView output;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.linear_notes);

        firstNameTXT = findViewById(R.id.firstTXT);
        lastNameTXT = findViewById(R.id.lastTXT);
        cityNameTXT = findViewById(R.id.cityTXT);
        schoolNameTXT = findViewById(R.id.schoolTXT);
        brotherNameTXT = findViewById(R.id.broTXT);
        sisterNameTXT = findViewById(R.id.sisTXT);
        output = findViewById(R.id.output);
        generateBTN=findViewById(R.id.generator);

        generateBTN.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                generate();
            }
        });

    }
    private void generate(){

    String first = String.valueOf(firstNameTXT.getText());
    String last = String.valueOf(lastNameTXT.getText());
    String city = String.valueOf(cityNameTXT.getText());
    String school = String.valueOf(schoolNameTXT.getText());
    String brother = String.valueOf(brotherNameTXT.getText());
    String sister = String.valueOf(sisterNameTXT.getText());


    //generate random thing
    int rF = (int)(Math.random()*first.length());
    int rL = (int)(Math.random()*last.length());
    int rC = (int)(Math.random()*city.length());
    int rS = (int)(Math.random()*school.length());
    int rB = (int)(Math.random()*brother.length());
    int rSi = (int)(Math.random()*sister.length());

    //generate scifi first name
    String scifiFirst= (first.substring(0,rF)+last.substring(rL));

    //generate scifi last name
    String scifiLast = (city.substring(0,rC)+school.substring(rS));

    //generate scifi home name
    String scifiHome = (brother.substring(rB)+sister.substring(0,rSi));

    //print out a welcome statment
    output.setText(String.format("welcome %s %s from %s",scifiFirst,scifiLast,scifiHome));
    }
 }
