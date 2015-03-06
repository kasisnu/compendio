package com.example.clientapp;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;

import org.apache.http.HttpResponse;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.InputStreamEntity;
import org.apache.http.impl.client.DefaultHttpClient;



import android.net.Uri;
import android.os.Bundle;
import android.os.Environment;
import android.provider.MediaStore;
import android.util.Log;
import android.view.Menu;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.Toast;
import android.app.Activity;
import android.app.AlertDialog;
import android.content.DialogInterface;
import android.content.Intent;
import android.database.Cursor;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;

public class MainActivity extends Activity implements OnClickListener{
	ImageView viewImage;
    Button b,button2;
    EditText edt;
    String userUrl;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
       button2=(Button)findViewById(R.id.button2);
       button2.setOnClickListener(this);
       
        b=(Button)findViewById(R.id.button1);
	      viewImage=(ImageView)findViewById(R.id.imageView1);
	     // gd = new GestureDetector(this);
	      b.setOnClickListener(new OnClickListener() {
			
			@Override
			public void onClick(View v) {
				// TODO Auto-generated method stub
				 selectImage();
			}
		});
        
    }
    private void selectImage() {
		 
        final CharSequence[] options = { "Take Photo", "Choose from Gallery","Cancel" };
 
        AlertDialog.Builder builder = new AlertDialog.Builder(MainActivity.this);
        builder.setTitle("Add Photo!");
        builder.setItems(options, new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int item) {
                if (options[item].equals("Take Photo"))
                {
                    Intent intent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
                    File f = new File(android.os.Environment.getExternalStorageDirectory(), "temp.jpg");
                    intent.putExtra(MediaStore.EXTRA_OUTPUT, Uri.fromFile(f));
                    startActivityForResult(intent, 1);
                }
                else if (options[item].equals("Choose from Gallery"))
                {
                    Intent intent = new   Intent(Intent.ACTION_PICK,android.provider.MediaStore.Images.Media.EXTERNAL_CONTENT_URI);
                    startActivityForResult(intent, 2);
 
                }
                else if (options[item].equals("Cancel")) {
                    dialog.dismiss();
                }
            }
        });
        builder.show();
    }

  @Override
protected void onActivityResult(int requestCode, int resultCode, Intent data) {
		 String path ;
	// TODO Auto-generated method stub
	super.onActivityResult(requestCode, resultCode, data);
	 if (resultCode == RESULT_OK) {
	
         if (requestCode == 1) {
        	
             File f = new File(Environment.getExternalStorageDirectory().toString());
             for (File temp : f.listFiles()) {
                 if (temp.getName().equals("temp.jpg")) {
                     f = temp;
                     break;
                 }
             }
             try {
                 Bitmap bitmap;
                 BitmapFactory.Options bitmapOptions = new BitmapFactory.Options();

                 bitmap = BitmapFactory.decodeFile(f.getAbsolutePath(),
                         bitmapOptions); 
                 ///viewImage.setImageBitmap(bitmap);
                
                 path = android.os.Environment
                         .getExternalStorageDirectory()
                         + File.separator
                         + "Phoenix" + File.separator + "default";
                 f.delete();
                 OutputStream outFile = null;
                 File file = new File(path, String.valueOf(System.currentTimeMillis()) + ".jpg");
                 viewImage.setImageBitmap(bitmap);

                 
                String url = userUrl;
                 //File f1=new File(path);
                 String str1=file.getName();
                  File file1 = new File(Environment.getExternalStorageDirectory(),
                 	        str1);
                  try {
                      
                 	 HttpClient httpclient = new DefaultHttpClient();

                      HttpPost httppost = new HttpPost(url);

                      InputStreamEntity reqEntity = new InputStreamEntity(
                              new FileInputStream(file1), -1);
                      reqEntity.setContentType("binary/octet-stream");
                      reqEntity.setChunked(true); // Send in multiple parts if needed
                      httppost.setEntity(reqEntity);
                      HttpResponse response = httpclient.execute(httppost);
                      //Do something with response...
                      String str=response.toString();
                      edt=(EditText)findViewById(R.id.editText1);
                      edt.setText(str);
                      
                  } catch (Exception e) {
                      // show error
                  }
                 try {
                     outFile = new FileOutputStream(file);
                     bitmap.compress(Bitmap.CompressFormat.JPEG, 85, outFile);
                     outFile.flush();
                     outFile.close();
                 } catch (FileNotFoundException e) {
                     e.printStackTrace();
                 } catch (IOException e) {
                     e.printStackTrace();
                 } catch (Exception e) {
                     e.printStackTrace();
                 }
             } catch (Exception e) {
                 e.printStackTrace();
             }
         
             

         } 
         else if (requestCode == 2) {
             Uri selectedImage = data.getData();
             String[] filePath = { MediaStore.Images.Media.DATA };
             /*File file = new File(Environment.getExternalStorageDirectory(),
            	        "filepath");*/
           Cursor c = getContentResolver().query(selectedImage,filePath, null, null, null);
             c.moveToFirst();
             int columnIndex = c.getColumnIndex(filePath[0]);
             String picturePath = c.getString(columnIndex);
             c.close();
             
             String url = userUrl;
             File f1=new File(picturePath);
             String str1=f1.getName();
              File file1 = new File(Environment.getExternalStorageDirectory(),
             	        str1);
              try {
                  
             	 HttpClient httpclient = new DefaultHttpClient();

                  HttpPost httppost = new HttpPost(url);

                  InputStreamEntity reqEntity = new InputStreamEntity(
                          new FileInputStream(file1), -1);
                  reqEntity.setContentType("binary/octet-stream");
                  reqEntity.setChunked(true); // Send in multiple parts if needed
                  httppost.setEntity(reqEntity);
                  HttpResponse response = httpclient.execute(httppost);
                  //Do something with response...
                  String str=response.toString();
                  edt=(EditText)findViewById(R.id.editText1);
                  edt.setText(str);
                  
              } catch (Exception e) {
                  // show error
              }
             
             Bitmap thumbnail = (BitmapFactory.decodeFile(picturePath));
             Log.w("path of image from gallery......******************.........", picturePath+"");
             viewImage.setImageBitmap(thumbnail);       
            
         }     
}
	 
}
    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.activity_main, menu);
        return true;
    }
	@Override
	public void onClick(View v) {
		getURL();
		// TODO Auto-generated method stub
		
	}
	private void getURL() {
		final AlertDialog.Builder alert = new AlertDialog.Builder(this);
		alert.setTitle("Set URL");
	    final EditText input = new EditText(this);
	    alert.setView(input);
	    alert.setPositiveButton("Ok", new DialogInterface.OnClickListener() {
	        public void onClick(DialogInterface dialog, int whichButton) {
	            String value = input.getText().toString().trim();
	            userUrl=input.getText().toString();
	            Toast.makeText(getApplicationContext(), value, Toast.LENGTH_SHORT).show();
	        }
	    });

	    alert.setNegativeButton("Cancel", new DialogInterface.OnClickListener() {
	        public void onClick(DialogInterface dialog, int whichButton) {
	            dialog.cancel();
	        }
	    });
	    alert.show();     // TODO Auto-generated method stub
		
	}

	
    
}
