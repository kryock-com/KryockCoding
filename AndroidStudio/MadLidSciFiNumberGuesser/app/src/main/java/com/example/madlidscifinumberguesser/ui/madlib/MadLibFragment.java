package com.example.madlidscifinumberguesser.ui.madlib;


import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;

import com.example.madlidscifinumberguesser.R;

public class MadLibFragment extends Fragment {
    EditText noun1;
    LinearLayout madlibPack;
    EditText verb1;
    EditText adverb1;
    EditText pnoun1;
    EditText noun2;
    EditText verb2;
    EditText adverb2;
    EditText pnoun2;

    Button generateBTN;
    Button restartBTN;
    TextView output;

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        super.onCreateView(inflater, container, savedInstanceState);
        View rootView = inflater.inflate(R.layout.fragment_madlib,container,false);

        noun1 = rootView.findViewById(R.id.noun1TXT);
        verb1 = rootView.findViewById(R.id.verb1TXT);
        adverb1 = rootView.findViewById(R.id.Adverb1TXT);
        pnoun1 = rootView.findViewById(R.id.plural1TXT);
        noun2 = rootView.findViewById(R.id.noun2TXT);
        verb2 = rootView.findViewById(R.id.verb2TXT);
        adverb2 = rootView.findViewById(R.id.Adverb2TXT);
        pnoun2 = rootView.findViewById(R.id.plural2TXT);

        madlibPack =rootView.findViewById(R.id.linearLayout);

        generateBTN = rootView.findViewById(R.id.generator);
        restartBTN = rootView.findViewById(R.id.restartBTN);
        output = rootView.findViewById(R.id.output);

        generateBTN.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                generate();
                madlibPack.setVisibility(view.INVISIBLE);
                output.setVisibility(view.VISIBLE);
                restartBTN.setVisibility(view.VISIBLE);
            }
        });
        restartBTN.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

            }
        });

        return rootView;
    }
    private void generate(){
        String noun1TXT = String.valueOf(noun1.getText());
        String verb1TXT = String.valueOf(verb1.getText());
        String adverb1TXT = String.valueOf(adverb1.getText());
        String pnoun1TXT = String.valueOf(pnoun1.getText());
        String noun2TXT = String.valueOf(noun1.getText());
        String verb2TXT = String.valueOf(verb1.getText());
        String adverb2TXT = String.valueOf(adverb1.getText());
        String pnoun2TXT = String.valueOf(pnoun1.getText());

        int paragraph = (int)(Math.random()*3);

        String madlib1 = "O say, can you "+verb1TXT+", by the dawn's early "+noun2TXT+", " +
                "What so "+adverb1TXT+" we hailed at the twilight's last gleaming, Whose broad " +
                ""+pnoun2TXT+" and bright stars, through the perilous fight, O'er the "+pnoun1TXT+" " +
                "we watched, were so gallantly streaming? And the rockets' red glare, the bombs " +
                "bursting in "+noun1TXT+", Gave proof through the night that our flag was still " +
                "there. O say, does that star spangled banner "+verb2TXT+" wave O'er the land of " +
                "the free and the home of the "+adverb2TXT+"?";
        String madlib2 = "One day, two best friends were walking on a lonely and dangerous path " +
                "through a "+noun2TXT+". As the sun began to set, they grew "+adverb2TXT+" but held " +
                "on to each other. Suddenly, they saw a "+noun1TXT+" in their path. One of the " +
                ""+pnoun1TXT+" ran to the nearest tree and "+adverb1TXT+" it in a jiffy. The other " +
                "boy did not know how to "+verb2TXT+" the tree by himself, so he "+verb1TXT+" on the " +
                "ground, pretending to be dead. The bear approached the boy on the ground and sniffed " +
                "around his head. After appearing to whisper something in the boy’s ear, the bear went " +
                "on its way. The boy on the tree climbed down and asked his friend what the bear had " +
                "whispered in his ear. He replied, “Do not trust "+pnoun2TXT+" who do not care for you.”";
        String madlib3 = "On a hot day, a "+noun2TXT+" in the "+noun1TXT+" started feeling hungry. " +
                "He was starting to "+verb1TXT+" for his food when he found a hare roaming around " +
                "alone. Instead of catching the hare, the "+noun2TXT+" let it go – “A small hare such " +
                "as this can’t "+pnoun1TXT+" my hunger”, he said and scoffed. Then, a beautiful deer " +
                "passed by and he decided to take his chances – he "+verb2TXT+" and "+verb2TXT+" behind " +
                "the deer but since he was weak because of the hunger, he struggled to keep up with the " +
                "deer’s speed. Tired and defeated, the "+noun2TXT+" went back to look for the hare to fill " +
                "up his stomach for the time being, but it was gone. The "+noun2TXT+" was sad and remained " +
                "hungry for a long time.";

        String mainMadLib;

        if (paragraph == 0){

            output.setText(madlib1);
        }
        else if (paragraph == 1){
            output.setText(madlib2);
        }
        else{
            output.setText(madlib3);
        }

    }
}
