package com.example.dice;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

import java.util.Random;

public class MainActivity extends AppCompatActivity {
    //global variable
    private ImageView imageViewDice;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main); //connection xml file to java
        //assigning the global variable
        imageViewDice = findViewById(R.id.image_view_dice);
        //onClick for d4
        imageViewDice.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                rollD4();
            }
        });
        //onClick for d6
        imageViewDice.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                rollD6();
            }
        });
        //onClick for d8
        imageViewDice.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                rollD8();
            }
        });
        //onClick for d10
        imageViewDice.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                rollD10();
            }
        });
        //onClick for d12
        imageViewDice.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                rollD12();
            }
        });
        //onClick for d20
        imageViewDice.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                rollD20();
            }
        });
    }

    //Generate a random number and show that dice number
    public void rollD4(){
        //random.randint(1,4)
        Random rng = new Random();
        int randomNumber = rng.nextInt(4)+1;
        /*
        if(randomNumber==1){
            imageViewDice.setImageResource(R.drawable.dice1);
        }
        */
        imageViewDice.setImageResource(R.drawable.image ());
        TextView numText = findViewById(R.id.numbertextView);
        numText.setText(randomNumber);        }

    public void rollD6(){
        //random.randint(1,6)
        Random rng = new Random();
        int randomNumber = rng.nextInt(6)+1;
        /*
        if(randomNumber==1){
            imageViewDice.setImageResource(R.drawable.dice1);
        }
        */
        imageViewDice.setImageResource(R.drawable.square);
        TextView numText = findViewById(R.id.numbertextView);
        numText.setText(randomNumber);    }

    public void rollD8(){
        //random.randint(1,8)
        Random rng = new Random();
        int randomNumber = rng.nextInt(8)+1;
        /*
        if(randomNumber==1){
            imageViewDice.setImageResource(R.drawable.dice1);
        }
        */
        imageViewDice.setImageResource(R.drawable.TRiangel);
        TextView numText = findViewById(R.id.numbertextView);
        numText.setText(randomNumber);    }

    public void rollD10(){
        //random.randint(1,10)
        Random rng = new Random();
        int randomNumber = rng.nextInt(10)+1;
        /*
        if(randomNumber==1){
            imageViewDice.setImageResource(R.drawable.dice1);
        }
        */
        imageViewDice.setImageResource(R.drawable.TRiangel);
        TextView numText = findViewById(R.id.numbertextView);
        numText.setText(randomNumber);    }

    public void rollD12(){
        //random.randint(1,12)
        Random rng = new Random();
        int randomNumber = rng.nextInt(12)+1;
        /*
        if(randomNumber==1){
            imageViewDice.setImageResource(R.drawable.dice1);
        }
        */
        imageViewDice.setImageResource(R.drawable.square);
        TextView numText = findViewById(R.id.numbertextView);
        numText.setText(randomNumber);    }

    public void rollD20(){
        //random.randint(1,20)
        Random rng = new Random();
        int randomNumber = rng.nextInt(20)+1;
        /*
        if(randomNumber==1){
            imageViewDice.setImageResource(R.drawable.dice1);
        }
        */
        imageViewDice.setImageResource(R.drawable.TRiangel);
        TextView numText = findViewById(R.id.numbertextView);
        numText.setText(randomNumber);
    }


}