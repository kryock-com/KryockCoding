package com.example.madlidscifinumberguesser.ui.numberguesser;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;

import com.example.madlidscifinumberguesser.R;

public class NumberguesserFragment extends Fragment {
    EditText editid;
    TextView textView;
    Button guessBTN;
    TextView points;
    TextView tries;


    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        super.onCreateView(inflater, container, savedInstanceState);
        View rootView = inflater.inflate(R.layout.fragment_numberguesser, container, false);
        editid = rootView.findViewById(R.id.editId);
        textView = rootView.findViewById(R.id.textView2);
        guessBTN = rootView.findViewById(R.id.guessBTN);
        points = rootView.findViewById(R.id.pointsTXT);
        tries = rootView.findViewById(R.id.triesTXT);



        int randomNum =(int)((Math.random() * (100 - 1)) + 1);
        guessBTN.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                numGuesser(randomNum);
            }

        });
        return rootView;
    }
    public void numGuesser(int randomNum){
        int userGuessing;
        int numOfGuesses = 5;
        int point = Integer.parseInt(points.getText().toString());
        int numOfTries = Integer.parseInt(tries.getText().toString());

        boolean winOrLose=false;

        userGuessing = Integer.parseInt(editid.getText().toString());

            if (userGuessing < randomNum) {
                Toast toast = Toast.makeText(getContext(), "Think of Higher Number, Try Again", Toast.LENGTH_SHORT);
                toast.show();

                winOrLose = false;
                numOfTries-=1;
                while(numOfTries <= 0){
                    editid.setVisibility(editid.INVISIBLE);
                }
                tries.setText(String.valueOf(numOfTries));
                points.setText(String.valueOf(point));
            }
            else if (userGuessing > randomNum) {
                Toast toast = Toast.makeText(getContext(), "Think of Lower Number, Try Again", Toast.LENGTH_SHORT);
                toast.show();

                winOrLose = false;
                numOfTries-=1;
                while(numOfTries <= 0){
                    editid.setVisibility(editid.INVISIBLE);
                }
                tries.setText(String.valueOf(numOfTries));
                points.setText(String.valueOf(point));
            }
            else {
                Toast toast = Toast.makeText(getContext(), "Congratulations, You Got the Number", Toast.LENGTH_SHORT);
                point += 50;
                toast.show();

                winOrLose = true;

                if(numOfGuesses>0){
                    point+=5*numOfGuesses;
                }

                points.setText(String.valueOf(point));
                textView.setText("I am thinking of a new number between 1 to 100. Can you guess what it is ?");
            }

    }


}

