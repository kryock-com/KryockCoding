package com.example.helloworld;
//package is a folder to tell android where the file is at

//the library with all of the functions for basic android apps
import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;


//every file needs a class - this one uses the AppCompatActivity library
public class MainActivity extends AppCompatActivity {

    @Override   //what to do when the page opens
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    //create a function that says hello to the user
    public void sayHello(View v){
        //view is the library that will in passing info back and forth

        //nameEnter = widgetName.get()
        EditText nameEntered = findViewById(R.id.nameEditView);
        TextView greetText = findViewById(R.id.helloText);

        //infoFromWidget = ""
        String infoFromWidget = (String) nameEntered.getText().toString();
        greetText.setText("Hi "+ infoFromWidget +", nice to meet you");
    }

}

