��    `        �         (  
   )     4     A     O     `     n     |     �     �     �     �     �  
   �  	   �  
   �     �     �     �     �     	     	     	     #	  	   (	     2	     7	     ?	  	   D	     N	  	   S	     ]	  	   b	  	   l	     v	     {	     �	     �	     �	     �	     �	     �	     �	     �	     �	     �	  
   �	     �	     �	     �	     �	     �	     
     
  	   
     
     &
     /
     8
     A
     N
  
   S
  
   ^
  
   i
     t
     y
     
     �
     �
     �
     �
     �
     �
     �
     �
  
   �
     �
  
   �
  
                  )     7  	   E  
   O     Z  
   g     r          �  	   �     �     �     �     �     �  B  �  
                  ,     =     K     Y     ^     c     l     �     �  *   �     �     �     �  
   �  �   �  �   �  �   �     �  �   �       �  #     �     �        �          �          �   !  �     H   �     �     �     �       '     -   G     u     �     �     �     �     �     �          0     D     I  
   V  [   a  �   �     q     �     �     �     �     �  f  �  �  B  b  =     �     �     �  t   �     [  a   j     �     �  A  �     ;!  U   O!  	  �!     �"  o   �"  {   /#     �#  ;   �#     �#  7    $     8$     P$     `$     n$     }$     �$     �$     �$     �$  �   �$  %   �%     �%      �%             ^   9      	   =   )   0   *   2      :      ;         +      5   T             $          (   C       D   J                 7              ?   V           H         -          L   Q   #       K   P       6   I   ]               G   Y      _   [       E                   1   S          
   X   A       M   3       >             @   .   R       '       N                    B   O   "       W   <       U           F   `       \       4          ,          Z   8   !       /   %   &    action_add action_close action_delete action_duplicate action_export action_import action_next action_page action_prev action_template actions app ask_delete back_list btn_upload btnok codec convert_list_to_dict convert_to_base64 data descc download esp1 esp1_parr esp2 especif exp1 exp1_desc exp2 exp2_desc exp3 exp3_desc extension file format format1 format2 format3 format_image holderd holderf holdern lang_change msg_noreport nameC not_format opt1 opt2 opt3 opt4 options param path path_json report_temp seccion1 seccion2 seccion3 subtitle_add tem1 tem1_parr1 tem1_parr2 tem1_parr3 tem2 tem21 tem21_1parr1 tem21_1parr2 tem21_2parr1 tem21_2parr2 tem21_2parr3 tem21_3parr1 tem21_3parr2 tem22 tem22_parr1 tem2_parr1 tem3 tem3_parr1 tem3_parr2 template template_code template_edit template_name title_add title_add1 title_delete title_edit title_import title_import1 titledoc titledoc1 titlep to_dict unique updatec warn_import Project-Id-Version: PACKAGE VERSION
Report-Msgid-Bugs-To: 
PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE
Last-Translator: FULL NAME <EMAIL@ADDRESS>
Language-Team: LANGUAGE <LL@li.org>
Language: 
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
Plural-Forms: nplurals=2; plural=(n != 1);
 Add report Close Delete report Duplicate report Export report Import report Next Page Previous Update template of report Actions Reports Administration Are you sure to want to delete the report  Return to the list Upload Submit Using code  <b>convert_list_to_dict()</b>: This helper function receives as a parameter a query made with a database model and converts it into a list or collection of dictionaries to be used by a report. It only allows the conversion of those simple fields. <b>convert_to_base64(path, format_image)</b>:This function can be used to convert any image to base 64 format. This format is necessary for the image to display smoothly in the report. Context used as a dictionary. This is the information that will be rendered in the report. Each name of the variables in the context must match its equivalent in the parameters defined in the model template design. Description If the variable is set to True, the pdf report will be downloaded directly without being viewed, otherwise the pdf will be displayed. Data Formats ReportBro reports accept data using a dictionary or context (such as a view function). Each parameter of the context, therefore, is defined with its name (unrepeatable data that must coincide with the one defined during the design of the report) and its information (a text, number, date, image, simple list of elements or objects). Objects within a list must be defined as a dictionary so that the Report can recognize their attributes. Export Modes Template (Format in JSON) Export by Code <b>export_report_by_code(template_code, data, extension='pdf', file='report')</b>: This function allows the programmer to render a report (in the database) using mainly its code (record code that is always unique) and the data passed as context. Export by Name <b>export_report_by_name(template_code, data, extension='pdf', file='report')</b>: This function allows the programmer to render a report (in the database) using mainly its name (record name that will always be unique) and the data passed as context. Export using JSON <b>export_report_from_JSON(path_json, data, extension='pdf', file='report')</b>: This feature allows the programmer to render an exported report in a separate JSON file using its specific path and the data passed as context. Parameter that supports only two input values (pdf - xlsx). By default it is always pdf. This is the format in which the report will be exported. Name of the report file when exported. By default it is set to 'report'. Format Options Convert to list Convert to dictionary Adjust Image Image format, only allows .png and .jpg Provide an overview of the report's function. Select a JSON template. Enter the report's name. Change Language There's not report records Name Format file is not suitable. Reportbro Admin Documentation Tutorial on ReportBro Designer Site Administration Home Main Options Parameters Image-specific path. Only its relative path can be used according to the project structure. Specific path of the JSON-formatted file. (This file is generated with the 'Export' function of this app.) Its relative path can be used depending on the structure of the project. Editing report's template What's Reportbro Compatibility Specifications New Library of ReportBro Designer Designer is a JavaScript plugin that can be integrated into your web application. Although this requires a little more work at first, having a built-in template design tool has quite a few benefits as you will discover by reading. Installation is simple by including some JavaScript libraries and initializing the Designer with some HTML and JavaScript code. It is optimized for simple reporting, that is, to display data (text, tabular data, or images) exactly as defined in a design template. All parameters are passed directly to the report and therefore <b>ReportBro </b> does not require knowledge of SQL (or another query language) to create a report. In contrast, using the same data requests in the underlying web application and for reporting eliminates the risk of potential inconsistencies between the data displayed on the screen and the printed report. <b> ReportBro</b> allows you to easily and quickly design reports with a perfect design. Printing the current page in the footer is as simple as inserting predefined variables for the current page and total page count. Even to generate Excel outputs no additional configuration is needed because ReportBro has a very clear structure and is easy to learn. Library of reportbro-lib Libraries Used ReportBro Designer Javascript The free version of <b>ReportBro Designer</b> was used, so only the functions available in that version can be used. Code Reference <b>This app is an enhanced version of the Albumsreport sample created for ReportBro Designer.</b> Original version available in  Reportbro-lib It generates pdf and xlsx reports, Supports (repetitions) header and footer, Allows predefined and own formats for the pages of the report, Uses the elements: Texts, line, image, barcodes, tables, break pages and sections, Allows the stylization of texts and elements and can evaluate expressions and define conditionals. Supported Databases <b> It supports all adjustable databases for Django: SQLite, Postgres, MySQL, etc</b> <b> ReportBro-lib</b> is a library for generating PDF and XLSX reports written in Python for use in conjunction with <b>Django</b>. Report templates can be created with <b>ReportBro Designer</b>, a Javascript plugin that can be integrated into your web application. ReportBro Admin <b>A free project that unites the JavaScript libraries of ReportBro designer and the reportbro-lib library.</b> This project is a django app that allows the administration and easy integration of all the libraries related to ReportBro. Template Use code of the report that was inserted into the database. Update template Name of the report that was inserted into the database. New report registration Creating Report Remove report Editing Report Import report Import Documentation ReportBro Admin Documentation Reports <b>to_dict()</b>: This helper function can convert each instance of a passed Model class as a parameter into a key-value dictionary understandable by the report. It only allows the conversion of those simple fields. A report name is repeated. Change it. Modified The file extension must be .json 