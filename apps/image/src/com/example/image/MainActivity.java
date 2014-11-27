package com.example.image;


import android.os.Bundle;
import android.app.Activity;
import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.graphics.Matrix;
import android.graphics.PointF;
import android.graphics.RectF;
import android.util.Log;
import android.view.Menu;
import android.view.MotionEvent;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.Toast;

public class MainActivity extends Activity {
	static final int DRAG = 1;
	
	Matrix matrix = new Matrix();

	Matrix savedMatrix = new Matrix();
	
	int mode = 0;
	
	PointF start = new PointF();

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
		final ImageView image=(ImageView)findViewById(R.id.imageView1);
		
		
		

	    final Bitmap icon = BitmapFactory.decodeResource(this.getResources(),
	            R.drawable.text);
	    image.setImageBitmap(icon);
        image.setOnTouchListener(new View.OnTouchListener() {
			
			@Override
			public boolean onTouch(View v, MotionEvent event) {
				//ImageView view = (ImageView) v;


	            switch (event.getAction() & MotionEvent.ACTION_MASK)
	            {

	            case MotionEvent.ACTION_DOWN:     
	            	savedMatrix.set(matrix);

	                start.set(event.getX(), event.getY());

	                mode = DRAG;
	              
	                Log.i(null,"mode = drag and coordinates are x ="+event.getX()+" and y= "+event.getY());
	                Toast toast = Toast.makeText(getApplicationContext(),"Coordinates are x ="+event.getX()+" and y= "+event.getY(), Toast.LENGTH_LONG);
	                toast.show();
	                RectF r = new RectF();
	                matrix.mapRect(r);

	                break;
                  
	            
	            /*case MotionEvent.ACTION_DOWN:
	            	savedMatrix.set(matrix);
                    start.set(event.getX(), event.getY());
	            	int[] viewCoords=new int[2];
	            	image.getLocationOnScreen(viewCoords);
	            	Toast toast = Toast.makeText(getApplicationContext()," Screen Coordinates are x ="+viewCoords[0]+" and y= "+viewCoords[1],Toast.LENGTH_LONG);
		            toast.show();
	            	
	            	int x=(int)event.getX();
	            	int y=(int)event.getY();
	            	int imageX=x-viewCoords[0];
	            	int imageY=y-viewCoords[1];   
	            	
	            	Toast toast1 = Toast.makeText(getApplicationContext(),"Coordinates are x ="+imageX+" and y= "+imageY, Toast.LENGTH_LONG);
		            toast1.show();
		            
		            break;*/
	            	
	            }// TODO Auto-generated method stub
				return false;
			}
		});
	    
		
        
        
        
        
        
        Button button = (Button) findViewById(R.id.button1);
        button.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
            	Intent intent = new Intent("android.media.action.IMAGE_CAPTURE");
            	 startActivityForResult(intent, 0); // Perform action on click
            }
        });

	}

	private ImageView findViewById(ImageView image) {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.main, menu);
		return true;
	}

}
