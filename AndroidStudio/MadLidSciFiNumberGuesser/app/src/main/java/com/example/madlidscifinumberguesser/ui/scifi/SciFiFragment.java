package com.example.madlidscifinumberguesser.ui.scifi;


import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import com.example.madlidscifinumberguesser.R;


import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;

public class SciFiFragment extends Fragment {
    //defineing the widget variable
    EditText firstNameTXT;
    EditText lastNameTXT;
    EditText cityNameTXT;
    EditText schoolNameTXT;
    EditText brotherNameTXT;
    EditText sisterNameTXT;
    Button generateBTN;
    TextView output;

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        super.onCreateView(inflater, container, savedInstanceState);
        View rootView = inflater.inflate(R.layout.fragment_scifi,container,false);

        firstNameTXT = rootView.findViewById(R.id.firstTXT);
        lastNameTXT = rootView.findViewById(R.id.lastTXT);
        cityNameTXT = rootView.findViewById(R.id.cityTXT);
        schoolNameTXT = rootView.findViewById(R.id.schoolTXT);
        brotherNameTXT = rootView.findViewById(R.id.broTXT);
        sisterNameTXT = rootView.findViewById(R.id.sisTXT);
        generateBTN = rootView.findViewById(R.id.generator);
        output = rootView.findViewById(R.id.output);

        generateBTN.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                generate();
            }
        });

        return rootView;

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
