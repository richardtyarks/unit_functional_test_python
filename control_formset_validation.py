# https://careerkarma.com/blog/python-nested-dictionary/
def check_formset_validation(forms):
    distinct_resp_control = []
    distinct_date_control = []

    for key, form in forms.items():
        resp_control = form['resp_control']
        list_sapeur_in_control = [form['sap_tonne'], form['sap_renault'],
                                  form['sap_mercedes'], form['sap_mitsubishi']]
        date_control = form['date']
        if resp_control in distinct_resp_control:
            return 1

        if resp_control not in list_sapeur_in_control:
            return 2

        if date_control in distinct_date_control:
            return 3

        for sapeur in list_sapeur_in_control:
            ctn_sapeur = list_sapeur_in_control.count(sapeur)
            if ctn_sapeur > 1:
                return 4

        if len(date_control) != 10:
            return 5

        distinct_resp_control.append(resp_control)
        distinct_date_control.append(date_control)
    return 6
