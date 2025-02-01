package com.example.pizzaplanet;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {


    private RadioGroup sizeRG;
    private RadioButton smallRB;
    private RadioButton mediumRB;
    private RadioButton largeRB;
    private TextView output;
    private CheckBox chickCBox;
    private CheckBox bbqCBox;
    private CheckBox hamCBox;
    private Button outPutBTn;
    private double total;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);


        sizeRG=findViewById(R.id.radioGroup2);
        smallRB=findViewById(R.id.smallRadio);
        mediumRB=findViewById(R.id.mediumRadio);
        largeRB=findViewById(R.id.largeRadio);

        output=findViewById(R.id.outputLBL);

        chickCBox=findViewById(R.id.chickCB);
        bbqCBox=findViewById(R.id.bbqCB);
        hamCBox=findViewById(R.id.hamCB);

        outPutBTn=findViewById(R.id.outputBTN);

        outPutBTn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if(chickCBox.isChecked()){
                    //Toast.makeText(MainActivity.this,"Chicken",Toast.LENGTH_SHORT).show();
                    total+=17.98;
                }
                if(bbqCBox.isChecked()){
                    total+=17.98;
                }
                if(chickCBox.isChecked()){
                    total+=17.98;
                }
                onRadioButtonClicked();
                output.setText(Double.toString(total));
            }
        });
        sizeRG.setOnCheckedChangeListener(new RadioGroup.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(RadioGroup radioGroup, int id) {
                RadioButton rb =(RadioButton) sizeRG.findViewById(id);
            }
        });



    }
    public void onRadioButtonClicked(){
        Log.d("RadioButton Test","triggered");
        int selectedId = sizeRG.getCheckedRadioButtonId();
        if (selectedId == -1){
            Toast.makeText(MainActivity.this,"Choose a Size",Toast.LENGTH_SHORT).show();
        }
        else{
            RadioButton radioButton = (RadioButton) sizeRG.findViewById(selectedId);
            Toast.makeText(MainActivity.this,radioButton.getText(),Toast.LENGTH_SHORT).show();
            if (radioButton.getText().equals("Small")){
                total+=5;
            }
            else if (radioButton.getText().equals("Medium")){
                total+=6;
            }
            else{
                total+=7;
            }
        }
    }
}