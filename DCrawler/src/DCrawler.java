import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.PrintWriter;
import java.io.UnsupportedEncodingException;
import java.net.MalformedURLException;

import com.gargoylesoftware.htmlunit.BrowserVersion;
import com.gargoylesoftware.htmlunit.ElementNotFoundException;
import com.gargoylesoftware.htmlunit.FailingHttpStatusCodeException;
import com.gargoylesoftware.htmlunit.NicelyResynchronizingAjaxController;
import com.gargoylesoftware.htmlunit.WebClient;
import com.gargoylesoftware.htmlunit.html.HtmlAnchor;
import com.gargoylesoftware.htmlunit.html.HtmlForm;
import com.gargoylesoftware.htmlunit.html.HtmlPage;
import com.gargoylesoftware.htmlunit.html.HtmlSelect;


public class DCrawler {
	
	private static WebClient webClient;
	
	private static void setup(){
		webClient = new WebClient(BrowserVersion.FIREFOX_24);
		webClient.setAjaxController(new NicelyResynchronizingAjaxController());
	}
	
	private static void teardown(){
		webClient.closeAllWindows();
		webClient = null;
	}
	
	private static void toFile(String name, String text){
		try {
			PrintWriter writer;
			writer = new PrintWriter(name, "UTF-8");
			writer.println(text);
			writer.close();
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (UnsupportedEncodingException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	private static void crawl(String url){
		HtmlPage page;
		try {
			page = webClient.getPage(url);
		} catch (FailingHttpStatusCodeException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
			return;
		} catch (MalformedURLException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
			return;
		} catch (IOException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
			return;
		}
		HtmlForm form = page.getFormByName("win0");
		
		// TODO: iterate through options (terms/subjects). Not doing it yet
		// in order not to flood target site during testing.
		
		HtmlSelect instSelect = form.getSelectByName("CLASS_SRCH_WRK2_INSTITUTION$42$");
		instSelect.setSelectedAttribute(instSelect.getOption(1), true);
		HtmlSelect termSelect = form.getSelectByName("CLASS_SRCH_WRK2_STRM$45$");
		termSelect.setSelectedAttribute(termSelect.getOption(1), true);
		HtmlSelect subjSelect = form.getSelectByName("SSR_CLSRCH_WRK_SUBJECT_SRCH$0");
		subjSelect.setSelectedAttribute(subjSelect.getOption(1), true);
		HtmlAnchor searchAnchor = page.getAnchorByName("CLASS_SRCH_WRK2_SSR_PB_CLASS_SRCH");
		HtmlPage page2;
		try {
			page2 = searchAnchor.click();
			int i = 0;
			HtmlAnchor link;
			HtmlPage tmpPage;
			while(i < 99){
				try {
					link = page2.getAnchorByName("MTG_CLASS_NBR$" + i); 
				} catch(ElementNotFoundException enfe){
					break;
				}
				System.out.println("Processing: " + link.asText());
				tmpPage = link.click();
				toFile(link.asText()+".html", tmpPage.getElementById("PAGECONTAINER").asXml());
				i++;
			}
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	public static void main(String [] args){
		if(args.length < 1){
			System.out.println("Please provide target URL as an argument.");
			return;
		}
		setup();
		String the_url = args[0]; 
		crawl(the_url);
		teardown();
	}
}
