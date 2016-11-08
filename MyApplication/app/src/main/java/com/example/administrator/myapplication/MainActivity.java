package com.example.administrator.myapplication;

import android.app.Activity;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends Activity implements View.OnClickListener{


    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        setContentView(R.layout.activity_main);
        findViewById(R.id.hello).setOnClickListener(this);


    }


    @Override
    public void onClick(View v) {

        Toast.makeText(this,"aaaaaa",Toast.LENGTH_LONG).show();


    }
}
