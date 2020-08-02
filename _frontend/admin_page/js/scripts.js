document.querySelector('.add_account').addEventListener('click', (e)=>{
    document.querySelector('#main').innerHTML = render_signup_form()
});

function render_signup_form() {
    return `
    <div class="col-sm-2"></div>
    <div class="col-sm-4">
            <form role="form">
                    <div class="form-group">
                    <label class="required" for="user_name">
                        Akkauntun adı
                    </label>
                    <input type="text" class="form-control" id="username" required/>
                </div>

                <div class="form-group">
					 <label class="required" for="first_name">
						Ad
					</label>
					<input type="text" class="form-control" id="first_name" required/>
                </div>
                
                <div class="form-group">
					 <label class="required" for="last_name">
						Soyad
					</label>
					<input type="text" class="form-control" id="last_name" required/>
				</div>
                
                <div class="form-group">
					 <label class="required" for="email">
						Atasının adı
					</label>
					<input type="text" class="form-control" id="father_name" required/>
				</div>
                
                <div class="form-group">
					 
					<label class="required" for="password">
						Password
					</label>
					<input type="password" class="form-control" id="password" required/>
                </div>
        </div>
            <div class="col-sm-4">
                
                <div class="form-group">
					 <label for="Age" class="required">
						Topladiğı bal
					</label>
					<input type="text" class="form-control" id="points"/>
                </div>
                
                <div class="form-group">
					 <label for="phone_number" class="required">
						Bitirdiyi məktəb
					</label>
					<input type="text" class="form-control" id="school"/>
                </div>
                
                <div class="form-group">
					 <label for="country" class="required">
						Cinsiyyət
					</label>
					<input type="text" class="form-control" id="sex"/>
                </div>
                
                <div class="form-group">
					 <label for="City" class="required">
						Attestatən nömrəsi
					</label>
					<input type="text" class="form-control" id="attestat"/>
				</div>
                
                <div class="form-group">
                <label for="City" class="required">
                   Şəxsiyyət vəsiqəsinin nömrəsi
               </label>
               <input type="text" class="form-control" id="id_number"/>
           </div>
				<button type="submit" class="btn btn-primary submit_button">
					Submit
				</button>
			</form>
        </div>
        <div class="col-sm-2"></div>`;
};


document.querySelector('.remove_account').addEventListener('click', (e)=>{
    document.querySelector('#main').innerHTML = render_remove_account()
});

function render_remove_account() {
    return `
    <div class="col-sm-4"></div>
    <div class="col-sm-4">
            <form role="form">
                    <div class="form-group">
                    <label class="required" for="user_name">
                        Akkauntun adı
                    </label>
                    <input type="text" class="form-control" id="username" required/>
                </div>

                <div class="form-group">
					 <label class="required" for="first_name">
						Ad
					</label>
					<input type="text" class="form-control" id="first_name" required/>
                </div>
                
                <div class="form-group">
					 <label class="required" for="last_name">
						Soyad
					</label>
					<input type="text" class="form-control" id="last_name" required/>
				</div>
                
                <div class="form-group">
					 <label class="required" for="reason">
						Silinmə səbəbi
                    </label>
                    <input type="text" class="form-control" id="reason" required/>
                </div>
                <button type="submit" class="btn btn-primary submit_button">
                Submit
            </button>
            </form>
        </div>
                
    <div class="col-sm-4"></div>`;
};

