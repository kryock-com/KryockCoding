package com.example.intentexample;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class OtherActivity extends Activity {
    private Button other;
    private TextView otherLBL;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.other_activity);
        other = findViewById(R.id.OtherBTN);
        otherLBL = findViewById(R.id.OtherLBL);

        String valueOfIntent = getIntent().getStringExtra("User Input");
        otherLBL.setText(valueOfIntent);


        other.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent i = new Intent(OtherActivity.this,MainActivity.class);


                startActivity(i);
            }
        });

    }

}
